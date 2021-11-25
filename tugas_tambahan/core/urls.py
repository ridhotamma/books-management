from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-book/', views.add_book, name='add-book'),
    path('add-publisher/', views.add_publisher, name='add-publisher'),
    path('add-store/', views.add_store, name='add-store'),
    path('add-author/', views.add_author, name='add-author'),
]