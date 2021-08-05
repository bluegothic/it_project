from django import forms
from django.conf.urls import url
from django.db import models
from django.forms import fields
from django.template.defaultfilters import title
from django.contrib.auth.models import User
from rango.models import Page, Category, UserProfile, Comment


class CategoryForm(forms.ModelForm):
  name = forms.CharField(max_length=128, help_text="Please enter the title of your poll.")
  views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
  likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
  slug = forms.CharField(widget=forms.HiddenInput(), required=False)

  context = forms.CharField(max_length=512, help_text="Please enter the description.")
  choice1 = forms.CharField(max_length=128, help_text="Please enter the choice 1 .")
  choice2 = forms.CharField(max_length=128, help_text="Please enter the choice 2 .")
  choice3 = forms.CharField(max_length=128, help_text="Please enter the choice 3 .")

  class Meta:
    model = Category
    fields = ('name', 'context', 'choice1', 'choice2', 'choice3',)
    exclude = ('author_id', 'posttime', 'count1', 'count2', 'count3')

class PageForm(forms.ModelForm):
  title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
  url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
  views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)

  class Meta:
    model = Page
    exclude = ('category',)
  
  def clean(self):
    cleaned_data= self.cleaned_data
    url=cleaned_data.get('url')

    if url and not url.startswith('http://'):
      url = f'http//{url}'
      cleaned_data['url'] = url
    
    return cleaned_data

class UserForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput())

  class Meta:
    model = User
    fields = ('username', 'email','password',)

class UserProfileForm(forms.ModelForm):
  class Meta:
    model = UserProfile
    fields = ('website', 'picture',)

class contextForm(forms.ModelForm):
  context = forms.CharField(max_length=128, help_text="Please enter the comment.")

  class Meta:
    model = Comment
    exclude = ('comment_id', 'author_id', 'topic_id', 'date')

