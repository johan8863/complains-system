from django.urls import path
from . import views
from .api import endpoints

urlpatterns = [
    path('create/', views.ComplainCreate.as_view(), name='complains_create'),
    path('list/', views.ComplainList.as_view(), name='complains_list'),
    path('<int:pk>/detail/', views.ComplainDetail.as_view(), name='complains_detail'),
    path('<int:pk>/update/', views.ComplainUpdate.as_view(), name='complains_update'),
    path('<int:pk>/delete/', views.ComplainDelete.as_view(), name='complains_delete'),
]

urlpatterns_api = [
    path('api/listcreate/', endpoints.ComplainList.as_view(), name='api_complains_list_create'),
    path('api/<int:pk>/', endpoints.ComplainDetail.as_view(), name='api_complains_retrieve_update_delete'),
]

urlpatterns += urlpatterns_api