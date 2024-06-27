from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer
from rest_framework import serializers
from .models import Genre, Author, Book, Review

User = get_user_model()

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['book', 'user', 'rating', 'text']
        read_only_fields = ['user']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    genre = GenreSerializer()
    average_rating = serializers.ReadOnlyField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'description', 'publication_date', 'average_rating', 'slug']

class BookDetailSerializer(BookSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Book
        fields = BookSerializer.Meta.fields + ['reviews']
