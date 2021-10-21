from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apoblacion/', include('general.urls')),
    path('apoblacion/persons/', include('persons.urls')),
    path('apoblacion/promoters/', include('promoters.urls')),
    path('apoblacion/organisms/', include('organisms.urls')),
    path('apoblacion/entities/', include('entities.urls')),
    path('apoblacion/complains/', include('complains.urls')),
]