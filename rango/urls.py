from django.urls import path
from rango import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'rango'
urlpatterns = [
  path('', views.index, name='index'),
  path('poll/createpoll', views.add_poll, name='add_poll'),

  path('poll/<slug:topic_title_slug>/', views.show_poll, name='show_poll'),

  path('about/', views.about, name='about'),
  path('category/<slug:category_name_slug>/add_page/',views.add_page,name='add_page'),
  path('register/',views.register,name='register'),
  path('login/',views.user_login,name='login'),
  path('restricted/',views.restricted,name='restricted'),
  path('logout/',views.user_logout,name='logout'),
  path('category/<slug:category_name_slug>/add_comment/',views.add_comment,name='add_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)