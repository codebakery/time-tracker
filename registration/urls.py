from django.conf.urls import url, include

from . import views


urlpatterns = [
    # registration
    url('^$', views.Users.as_view(), name='users'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    ]