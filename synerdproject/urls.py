from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('synerd/', include('synerd.urls')),
    path('api/', include('synerd.api.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
