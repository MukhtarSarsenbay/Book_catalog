from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Genre, Author, Book, Review
from .serializers import GenreSerializer, AuthorSerializer, BookSerializer, BookDetailSerializer, ReviewSerializer
from django.shortcuts import render, get_object_or_404
from .models import Book, Genre, Author
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Book, Review
from .serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_favorites(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        user = request.user
        if book.favorited_by.filter(id=user.id).exists():
            book.favorited_by.remove(user)
            return Response({'status': 'removed from favorites'})
        else:
            book.favorited_by.add(user)
            return Response({'status': 'added to favorites'})
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def favorite_books(request):
    user = request.user
    favorite_books = user.favorite_books.all()
    serializer = BookSerializer(favorite_books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def book_reviews(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        reviews = Review.objects.filter(book=book)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    

def book_list(request):
    books = Book.objects.all()
    genres = Genre.objects.all()
    authors = Author.objects.all()
    
    genre_id = request.GET.get('genre')
    if genre_id:
        books = books.filter(genre_id=genre_id)

    author_id = request.GET.get('author')
    if author_id:
        books = books.filter(author_id=author_id)

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if start_date and end_date:
        books = books.filter(publication_date__range=[start_date, end_date])

    return render(request, 'books/book_list.html', {'books': books, 'genres': genres, 'authors': authors})

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'books/book_detail.html', {'book': book})


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BookDetailSerializer
        return BookSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
