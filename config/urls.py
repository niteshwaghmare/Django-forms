from boards import views
from django.contrib import admin
from django.urls import path, re_path
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^signup/$', accounts_views.signup, name='signup'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    re_path(r'^$', views.home, name='home'),
    re_path(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    re_path(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
]
