from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$', views.Records.as_view(), name='records'),
    url('^(?P<pk>[0-9]+)/$', views.RecordDetail.as_view(), name='record_detail'),
    ]
