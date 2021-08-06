from django.urls import path
from rango import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'rango'
urlpatterns = [
  path('', views.index, name='index'),
  path('myaccount/', views.myaccount, name='myaccount'),
  path('category/<slug:category_name_slug>/',views.show_category, name='show_category'),
  path('createpoll/', views.add_poll, name='createpoll'),
  path('category/<slug:category_name_slug>/add_page/',views.add_page,name='add_page'),
  path('register/',views.register,name='register'),
  path('login/',views.user_login,name='login'),
  path('restricted/',views.restricted,name='restricted'),
  path('logout/',views.user_logout,name='logout'),
  # path('category/<slug:category_name_slug>/add_comment/',views.add_comment,name='add_comment'),
  path('poll/',views.poll,name='poll'),
  path('test/',views.test,name='test'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)