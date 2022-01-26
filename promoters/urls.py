from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.PromoterCreate.as_view(), name='promoters_create'),
    path('list/', views.PromoterList.as_view(), name='promoters_list'),
    path('<int:pk>/detail/', views.PromoterDetail.as_view(), name='promoters_detail'),
    path('<int:pk>/update/', views.PromoterUpdate.as_view(), name='promoters_update'),
    path('<int:pk>/delete/', views.PromoterDelete.as_view(), name='promoters_delete'),
]