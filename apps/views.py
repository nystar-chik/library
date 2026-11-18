from django.shortcuts import render
from rest_framework.response import Response
from .serializer import BookSerializer, BookCreateSerializer, CategorySerializer, InfoSerializer, TegSerializer
from .models import Book, Category, Info, Teg
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from .paginator import BookPaginator
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins
from apps.mixins import ProMixinsGenericsAPI, ProMixinsDetailGenericsAPI
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPaginator
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET'])
    def expensive(self, request):
        book = Book.objects.order_by('-price').first()
        serializer = BookSerializer(book)
        return Response({'the most expensive book: ' : serializer.data})
    
    @action(detail=False, methods=['GET'])
    def cheap(self, request):
        book = Book.objects.order_by('price').first()
        serializer = self.get_serializer(book)
        return Response({'the most cheap book: ' : serializer.data})
    
    @action(detail=True, methods=['POST'])
    def change_reating(self, request, pk):
        book = self.get_object()
        book.rating = request.data.get(rating)
        book.save()
        return Response(book)
            
