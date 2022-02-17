from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout, name='logout'),
    path('welcome/', views.Welcome.as_view(), name='welcome'),
    path('persons/', include('persons.urls')),
    path('promoters/', include('promoters.urls')),
    path('organisms/', include('organisms.urls')),
    path('entities/', include('entities.urls')),
    path('complains/', include('complains.urls')),
]