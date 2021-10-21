from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.OrganismCreate.as_view(), name='organisms_create'),
    path('list/', views.OrganismList.as_view(), name='organisms_list'),
    path('<int:pk>/detail/', views.OrganismDetail.as_view(), name='organisms_detail'),
    path('<int:pk>/update/', views.OrganismUpdate.as_view(), name='organisms_update'),
    path('<int:pk>/delete/', views.OrganismDelete.as_view(), name='organisms_delete'),
]