from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout, name='logout'),
    path('welcome/', views.Welcome.as_view(), name='welcome'),
]