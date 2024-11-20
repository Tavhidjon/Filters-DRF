from rest_framework import serializers
from .models import Author, Genre, Book, Borrowing

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    genre = GenreSerializer()

    class Meta:
        model = Book
        fields = '__all__'

class BorrowingSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Borrowing
        fields = '__all__'
