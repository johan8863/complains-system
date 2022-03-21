from django.urls import path
from . import views
from .api import endpoints

urlpatterns = [
    path('create/', views.PromoterCreate.as_view(), name='promoters_create'),
    path('list/', views.PromoterList.as_view(), name='promoters_list'),
    path('<int:pk>/detail/', views.PromoterDetail.as_view(), name='promoters_detail'),
    path('<int:pk>/update/', views.PromoterUpdate.as_view(), name='promoters_update'),
    path('<int:pk>/delete/', views.PromoterDelete.as_view(), name='promoters_delete'),
]

urlpatterns_api = [
    path('api/listcreate/', endpoints.PromoterList.as_view(), name='api_promoters_list_create'),
    path('api/<int:pk>/', endpoints.PromoterDetail.as_view(), name='api_promoters_retrieve_update_delete'),
]

urlpatterns += urlpatterns_api