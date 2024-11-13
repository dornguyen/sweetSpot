from django.urls import path
from . import views

urlpatterns = [
    path('spots/', views.spot_list, name='spot-list'),
    path('spots/<int:pk>/', views.spot_detail, name='spot-detail'),
]