from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from core.heart_check import StatusCheck

prefix = 'v1/'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', StatusCheck.as_view(), name='health_check'),

]

docs = [
    path(prefix + 'docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(prefix + 'docs/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path(prefix + 'docs/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

translate = [
    path('translate/', include('translate.urls'), name='translate'),
]

api = [
    path(prefix + 'api/service/', include('services.urls'), name='service'),
]

urlpatterns += [
    *docs,
    *translate,
    *api,
]
