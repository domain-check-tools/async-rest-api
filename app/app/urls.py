from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

prefix = 'v1/'
urlpatterns = [
    path('admin/', admin.site.urls),
    path(prefix + 'docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(prefix + 'docs/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path(prefix + 'docs/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns += [
    path(prefix + 'api/', include('v1.urls'), name='v1'),
    path('health/', include('v1.heart_check'), name='healer_check'),
]
