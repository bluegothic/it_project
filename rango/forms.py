from django import forms
from django.conf.urls import url
from django.db import models
from django.forms import fields
from django.template.defaultfilters import title
from django.contrib.auth.models import User
from rango.models import Topic, UserProfile, Comment


class TopicForm(forms.ModelForm):
    dead_choice = (
        ('D', 'One Day'),
        ('W', 'One Week'),
        ('N', 'No End')
    )
    TYPES = (
        ('S', 'Single'),
        ('M', 'Multiple'),
    )
    type = forms.ChoiceField(widget=forms.RadioSelect, choices=TYPES, initial='S')
    context = forms.CharField(widget=forms.Textarea())
    option1 = forms.CharField(required=True)
    option2 = forms.CharField(required=True)
    option3 = forms.CharField(required=False)
    option4 = forms.CharField(required=False)
    option5 = forms.CharField(required=False)
    due = forms.ChoiceField(widget=forms.RadioSelect, choices=dead_choice, initial='D', label='Deadline')

    class Meta:
        model = Topic
        fields = ('title', 'context', 'type', 'option1', 'option2', 'option3', 'option4', 'option5')
        # exclude = ('author_id', 'posttime', 'count1', 'count2', 'count3')


class VoteForm(forms.ModelForm):
    pass
# class PageForm(forms.ModelForm):
#     title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
#     url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
#     views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
#
#     class Meta:
#         model = Page
#         exclude = ('category',)
#
#     def clean(self):
#         cleaned_data = self.cleaned_data
#         url = cleaned_data.get('url')
#
#         if url and not url.startswith('http://'):
#             url = f'http//{url}'
#             cleaned_data['url'] = url
#
#         return cleaned_data


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)


class ContextForm(forms.ModelForm):
    context = forms.CharField(max_length=128, help_text="Please enter the comment.")

    class Meta:
        model = Comment
        exclude = ('comment_id', 'author_id', 'topic_id', 'date')
