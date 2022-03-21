from django.urls import path
from . import views
from .api import endpoints

urlpatterns = [
    path('create/', views.OrganismCreate.as_view(), name='organisms_create'),
    path('list/', views.OrganismList.as_view(), name='organisms_list'),
    path('<int:pk>/detail/', views.OrganismDetail.as_view(), name='organisms_detail'),
    path('<int:pk>/update/', views.OrganismUpdate.as_view(), name='organisms_update'),
    path('<int:pk>/delete/', views.OrganismDelete.as_view(), name='organisms_delete'),
]

urlpatterns_api = [
    path('api/listcreate/', endpoints.OrganismList.as_view(), name='api_organisms_list_create'),
    path('api/<int:pk>/', endpoints.OrganismDetail.as_view(), name='api_organisms_retrieve_update_delete'),
]

urlpatterns += urlpatterns_api