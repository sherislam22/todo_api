from .serializers import (
    TodoListSerializer,
    CategorySerializer, 
    TodoListDetailSerializer,
    TodoListCreateSerializer,
)

from .models import Category, TodoList
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TodoListView(ListAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ['category', 'title']
    pagination_class = PageNumberPagination


class TodoDetailView(RetrieveAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListDetailSerializer

class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TotoListCreateView(CreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListCreateSerializer


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TodoListUpdateView(UpdateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListCreateSerializer


class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDestroyView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TodoListDestroyView(DestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListDetailSerializer


class TotoAPIView(APIView):
    @method_decorator(cache_page(60*60*2))
    def get(self, request):
        todolist = TodoList.objects.all()
        serializers = TodoListDetailSerializer(todolist, many=True)
        return Response(serializers.data)

