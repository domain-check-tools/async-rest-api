from django.urls import path, include

from v1.apps import V1Config

app_name = V1Config.name

dir_name = 'routers'

urlpatterns = [
    path('service/', include('{app_name}.{dir_name}.service.urls'.format(app_name=app_name, dir_name=dir_name))),

]
