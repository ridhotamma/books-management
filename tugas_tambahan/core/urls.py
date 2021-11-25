from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book-detail/<int:pk>/', views.book_detail, name='book-detail'),
    path('author-detail/<int:pk>/', views.author_detail, name='author-detail'),
    path('store-detail/<int:pk>/', views.store_detail, name='store-detail'),
    path('publisher-detail/<int:pk>/', views.publisher_detail, name='publisher-detail'),
    path('add-book/', views.add_book, name='add-book'),
    path('add-publisher/', views.add_publisher, name='add-publisher'),
    path('add-store/', views.add_store, name='add-store'),
    path('add-author/', views.add_author, name='add-author'),
]