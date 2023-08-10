from django.urls import path, include

from .apps import APIConfig

app_name = APIConfig.name

dir_name = 'endpoints'

urlpatterns = [
    path('service/', include('{app_name}.{dir_name}.service.urls'.format(app_name=app_name, dir_name=dir_name))),

]
