from django.conf.urls import url, include

from . import views


urlpatterns = [
    # registration
    url('^$', views.Users.as_view(), name='users'),
    url('^(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user_detail'),
    ]