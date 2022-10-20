from django.shortcuts import render
from rest_framework import generics
from rest.models import Book
from rest.serializers import BookSerializer
# Create your views here.

class BookList(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book
    serializer_class = BookSerializer