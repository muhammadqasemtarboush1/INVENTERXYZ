from django.contrib import admin
from django.urls import path
from django.urls.conf import include
# from django.conf.urls import url
# from rest_framework_swagger.views import get_swagger_view

# schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user_control.urls')),
    path('app/', include('app_control.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

