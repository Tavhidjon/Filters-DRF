from django.urls import path
from .views import *

urlpatterns = [
    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorDetailAPIView.as_view(), name='author-detail'),
    path('authors/<int:pk>/update/', AuthorUpdateAPIView.as_view(), name='author-update'),
    path('authors/<int:pk>/delete/', AuthorDeleteAPIView.as_view(), name='author-delete'),
    path('genres/', GenreListCreateAPIView.as_view(), name='genre-list-create'),
    path('genres/<int:pk>/', GenreDetailAPIView.as_view(), name='genre-detail'),
    path('genres/<int:pk>/update/', GenreUpdateAPIView.as_view(), name='genre-update'),
    path('genres/<int:pk>/delete/', GenreDeleteAPIView.as_view(), name='genre-delete'),
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', BookUpdateAPIView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteAPIView.as_view(), name='book-delete'),
    path('borrowings/', BorrowingListCreateAPIView.as_view(), name='borrowing-list-create'),
    path('borrowings/<int:pk>/', BorrowingDetailAPIView.as_view(), name='borrowing-detail'),
    path('borrowings/<int:pk>/update/', BorrowingUpdateAPIView.as_view(), name='borrowing-update'),
    path('borrowings/<int:pk>/delete/', BorrowingDeleteAPIView.as_view(), name='borrowing-delete'),
]
