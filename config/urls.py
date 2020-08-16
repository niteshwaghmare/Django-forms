from django.urls import path, re_path
from django.contrib import admin

from boards import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    path('admin/', admin.site.urls),
    # re_path(r'^signup/$', accounts_views.signuo, name="signup"),
]
