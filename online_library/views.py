from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Author, Genre, Book, Borrowing
from .serializers import AuthorSerializer, GenreSerializer, BookSerializer, BorrowingSerializer
from .filters import AuthorFilter, GenreFilter, BookFilter, BorrowingFilter


class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['name']
    search_fields = ['name']


class AuthorDetailAPIView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorUpdateAPIView(generics.UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDeleteAPIView(generics.DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ['name']
    filterset_class = GenreFilter


class GenreDetailAPIView(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreUpdateAPIView(generics.UpdateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDeleteAPIView(generics.DestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ['title', 'author__name', 'genre__name']
    filterset_class = BookFilter


class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateAPIView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteAPIView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BorrowingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ['book__title', 'borrower__name']
    filterset_class = BorrowingFilter


class BorrowingDetailAPIView(generics.RetrieveAPIView):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer


class BorrowingUpdateAPIView(generics.UpdateAPIView):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer


class BorrowingDeleteAPIView(generics.DestroyAPIView):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
