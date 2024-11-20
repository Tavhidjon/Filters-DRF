import django_filters
from .models import Author, Genre, Book, Borrowing

class AuthorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')  
    class Meta:
        model = Author
        fields = ['name']

class GenreFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains') 

    class Meta:
        model = Genre
        fields = ['name']

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author_name = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains')
    genre_name = django_filters.CharFilter(field_name='genre__name', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['title', 'author_name', 'genre_name']

class BorrowingFilter(django_filters.FilterSet):
    book_title = django_filters.CharFilter(field_name='book__title', lookup_expr='icontains')
    borrower_name = django_filters.CharFilter(field_name='borrower__name', lookup_expr='icontains')

    class Meta:
        model = Borrowing
        fields = ['book_title', 'borrower_name']
