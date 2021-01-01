from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from Book.serializers import BookDetailSerializer, BookListSerializer
from Book.models import Book
# Create your views here.


class BookCreateView(generics.CreateAPIView):
    serializer_class = BookDetailSerializer


class BookListView(generics.ListAPIView):
    serializer_class = BookListSerializer
    queryset = Book.objects.all()


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookDetailSerializer
    queryset = Book.objects.all()

