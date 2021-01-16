from django.shortcuts import get_object_or_404
from book.serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Book
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import action
from .models import Book
from .serializers import (
    BookDetailSerializer,
)


class BookViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving book.
    """
    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Book.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = BookDetailSerializer(user)
        return Response(serializer.data)
