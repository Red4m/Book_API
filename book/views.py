from rest_framework import generics, permissions, viewsets
from .models import Book

from .serializers import (
    BookDetailSerializer,
)


class BookCreateViewSet(viewsets.ModelViewSet):
    serializer_class = BookDetailSerializer


class BookListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()

    def get_class_serializer(self):
        if self.action == 'list':
            return BookDetailSerializer
        elif self.action == 'retrieve':
            return BookDetailSerializer

    serializer_class = BookDetailSerializer


class BookDetailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()

    def get_class_serializer(self):
        if self.action == 'list':
            return BookDetailSerializer
        elif self.action == 'retrieve':
            return BookDetailSerializer

    serializer_class = BookDetailSerializer
