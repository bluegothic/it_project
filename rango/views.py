from django import forms
from rango.forms import TopicForm, PageForm, UserForm, UserProfileForm, contextForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse, request
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rango.models import *
from datetime import datetime


def index(request):
    category_list = Topic.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    visitor_cookie_handler(request)

    poll_list = Topic.objects.order_by('-post_time')[:10]
    context_dict = {'polls': poll_list}
    print(poll_list)

    return render(request, 'rango/index.html', context=context_dict)


def myaccount(request):
    return render(request, 'rango/myaccount.html')

def poll(request):
    return render(request, 'rango/poll.html')

def show_category(request, category_name_slug):
    context_dict = {}
    # try:
    category = Topic.objects.get(slug=category_name_slug)
    pages = Page.objects.filter(category=category)

    context_dict['pages'] = pages
    context_dict['category'] = category

    print(pages.id)
    print(category.id)
    selections = TopicChooseDetail.objects.get(topic_id=category.id)
    # except Category.DoesNotExist:
    #     context_dict['pages'] = None
    #     context_dict['category'] = None

    return render(request, 'rango/category.html', context=context_dict)


def show_poll(request,topic_title_slug):
    context_dict = {}

    try:
        topic = Topic.objects.get(slug=topic_title_slug)
        comments = Comment.objects.filter(topic_id = topic)
        context_dict['comments'] = comments

    except topic.DoesNotExist:
        context_dict['comments'] = None
        context_dict['topic'] = None


    return render(request, 'rango/index.html', context=context_dict)



# @login_required
def add_poll(request):
    form = TopicForm()
    user = request.user

    if request.method == 'POST':
        form = TopicForm(request.POST)

        if form.is_valid():
            topic = form.save(commit=False)
            topic.author_id = user
            topic.cnt1 = 0
            topic.cnt2 = 0
            topic.cnt3 = 0
            topic.save()
            form.save(commit=True)

            return redirect('rango:index')
        else:
            print(form.errors)

    return render(request, 'rango/createpoll.html', {'form': form})


@login_required
def add_page(request, category_name_slug):
    try:
        category = Topic.objects.get(slug=category_name_slug)
    except Topic.DoesNotExist:
        category = None

    if category is None:
        return redirect('/rango/')

    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return redirect(reverse('rango:show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            print(form.errors)
    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context=context_dict)


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


def add_comment(request, category_name_slug):
    user = request.user
    try:
        category = Topic.objects.get(slug=category_name_slug)
    except:
        category = None

    if category is None:
        return redirect('/rango/')

    form = contextForm()

    if request.method == 'POST':
        form = contextForm(request.POST)

        if form.is_valid():
            if category:
                Comment = form.save(commit=False)
                Comment.topic_id = category
                Comment.author_id = user
                Comment.views = 0
                Comment.save()
                return redirect(reverse('rango:show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            print(form.errors)
    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_comment.html', context=context_dict)


def test(request):

    poll_list = Topic.objects.order_by('-post_time')[:10]
    context_dict = {'polls': poll_list}
    print(poll_list)
    return render(request, 'rango/test.html', context_dict)