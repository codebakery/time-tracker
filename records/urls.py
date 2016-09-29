from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$', views.Records.as_view(), name='records'),
    ]