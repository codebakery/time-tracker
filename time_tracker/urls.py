from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import renderers, response, schemas
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

from records import views as record_view


@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer, renderers.CoreJSONRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Pastebin API')
    return response.Response(generator.get_schema(request=request)) 


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/users/', include('registration.urls')),
    url(r'^api/records/', include('records.urls')),
    # Docs
    url(r'^docs/', schema_view),
    url(r'^$', record_view.Records.as_view())  # TODO: remove me when we have frontend
]
