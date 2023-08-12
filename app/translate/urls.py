from django.urls import path, include

from .apps import APIConfig

app_name = APIConfig.name

dir_name = 'endpoints'
location = '{app_name}.{dir_name}'.format(app_name=app_name, dir_name=dir_name)

urlpatterns = [

]
