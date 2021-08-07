from django import forms
from rango.forms import TopicForm, UserForm, UserProfileForm, CommentForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse, request
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rango.models import *
from datetime import datetime


def index(request):
    topic_list = Topic.objects.order_by('-likes')[:5]
    # page_list = Comment.objects.order_by('-views')[:5]

    # context_dict = {}
    # context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    # context_dict['categories'] = topic_list
    # context_dict['pages'] = page_list
    # visitor_cookie_handler(request)

    return render(request, 'rango/index.html', context={'topic_list': topic_list})


def myaccount(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'rango/myaccount.html', context=context_dict)


def show_poll(request, topic_title_slug):
    topic = Topic.objects.get(slug=topic_title_slug)
    comments = list(Comment.objects.filter(topic_id=topic.id))
    form = CommentForm()
    if request.method == 'POST':
        op = request.POST.get('poll')
        if op == 'op1':
            topic.cnt1 += 1
        elif op == 'op2':
            topic.cnt2 += 1
        elif op == 'op3':
            topic.cnt3 += 1
        elif op == 'op4':
            topic.cnt4 += 1
        elif op == 'op5':
            topic.cnt5 += 1
        topic.save()
    return render(request, 'rango/poll.html', context={'topic': topic, 'comments': comments, 'form':form})


@login_required
def add_poll(request):
    form = TopicForm()
    user = request.user

    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)

            # Handles the deadline.
            due = form.data.get('due')
            if due == 'D':
                topic.deadline = datetime.now() + timedelta(days=1)
            elif due == 'W':
                topic.deadline = datetime.now() + timedelta(weeks=1)
            else:
                topic.deadline = datetime.max
            # Handles the author_id.
            topic.author_user_id = user

            topic.save()
            return redirect('/rango/')
        else:
            print(form.errors)
    return render(request, 'rango/add_poll.html', {'form': form})


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'rango/register.html',
                  context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('rango:index'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print(f"Invalid login details: {username},{password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'rango/login.html')


@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")


@login_required
def user_logout(request):
    logout(request)

    return redirect(reverse('rango:index'))


def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits


@login_required()
def add_comment(request, topic_title_slug):
    try:
        topic = Topic.objects.get(slug=topic_title_slug)
    except:
        topic = None
    if topic is None:
        return redirect('/rango/')

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            # Comment.topic_id_id = topic

            # Comment.date = datetime.date(now())
            post.date = datetime.date(now())
            user = request.user
            post.author_user_id = user
            post.topic_id = topic
            # Comment.author_user_id_id = user
            # Comment.topic_id = category
            # Comment.author_id = user
            # Comment.views = 0
            post.save()
            # return redirect(reverse('rango:show_poll', kwargs={'topic_title_slug': topic_title_slug}))
            return redirect(reverse('rango:show_poll', kwargs={'topic_title_slug': topic_title_slug}))
        else:
            print(form.errors)
    # return redirect(reverse('rango:show_poll', kwargs={'topic_title_slug': topic_title_slug, 'form': form}))
    return render(request, 'rango:', context={'form': form})
