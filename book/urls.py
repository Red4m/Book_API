from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from book.views import *


app_name = 'book'
urlpatterns = format_suffix_patterns([
    path('create/', BookCreateViewSet.as_view({'post': 'create'})),
    path('all/', BookListViewSet.as_view({'get': 'list'})),
    path('all/<int:pk>/', BookDetailViewSet.as_view({'get': 'retrieve'})),
])
