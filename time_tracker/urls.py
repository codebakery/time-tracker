from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import renderers, response, schemas
from rest_framework.decorators import api_view, renderer_classes
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

from records import views as record_view
from registration import views as registration_view


@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer, renderers.CoreJSONRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Pastebin API')
    return response.Response(generator.get_schema(request=request))


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/token-auth/', registration_view.ObtainAuthToken.as_view()),
    url(r'^api/users/', include('registration.urls')),
    url(r'^api/records/', include('records.urls')),
    url(r'^api/projects/', record_view.Projects.as_view(), name='projects'),
    # Docs
    url(r'^docs/', schema_view),
    url(r'^$', record_view.Records.as_view())  # TODO: remove me when we have frontend
]
