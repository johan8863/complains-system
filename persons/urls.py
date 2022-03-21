from django.urls import path
from . import views

from .api import endpoints

urlpatterns = [
    path('create/', views.PersonCreate.as_view(), name='persons_create'),
    path('list/', views.PersonList.as_view(), name='persons_list'),
    path('<int:pk>/detail/', views.PersonDetail.as_view(), name='persons_detail'),
    path('<int:pk>/update/', views.PersonUpdate.as_view(), name='persons_update'),
    path('<int:pk>/delete/', views.PersonDelete.as_view(), name='persons_delete'),
]

urlpatterns_api = [
    path('api/listcreate/', endpoints.PersonList.as_view(), name='api_persons_list_create'),
    path('api/<int:pk>/', endpoints.PersonDetail.as_view(), name='api_persons_retrieve_update_delete'),
]

urlpatterns += urlpatterns_api