from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<slug:slug>/', views.book_detail, name='book_detail'),
    path('api/books/<int:pk>/favorite/', views.add_to_favorites, name='add_to_favorites'),
    path('api/reviews/', views.create_review, name='create_review'),
    path('api/users/me/favorites/', views.favorite_books, name='favorite_books'),
    path('api/books/<int:pk>/reviews/', views.book_reviews, name='book_reviews'),
]
