from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.EntityCreate.as_view(), name='entities_create'),
    path('list/', views.EntityList.as_view(), name='entities_list'),
    path('<int:pk>/detail/', views.EntityDetail.as_view(), name='entities_detail'),
    path('<int:pk>/update/', views.EntityUpdate.as_view(), name='entities_update'),
    path('<int:pk>/delete/', views.EntityDelete.as_view(), name='entities_delete'),
]