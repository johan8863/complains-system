from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('general.urls')),
    path('persons/', include('persons.urls')),
    path('promoters/', include('promoters.urls')),
    path('organisms/', include('organisms.urls')),
    path('entities/', include('entities.urls')),
    path('complains/', include('complains.urls')),
]