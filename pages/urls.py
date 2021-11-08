from django.urls import path
from .views import (
    CategoryListView,
    CategoryDetailView,
    TodoListView,
    TodoDetailView,
    CategoryCreateView,
    TotoListCreateView,
    TodoListUpdateView,
    CategoryUpdateView,
    CategoryDestroyView,
    TodoListDestroyView,
    TotoAPIView
)
urlpatterns = [
    path('todo/', TodoListView.as_view()),
    path('todo/<int:pk>/', TodoDetailView.as_view()),
    path('category/', CategoryListView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),
    path('category/create/', CategoryCreateView.as_view()),
    path('todo/create/', TotoListCreateView.as_view()),
    path('todo/<int:pk>/update/', TodoListUpdateView.as_view()),
    path('category/<int:pk>/update/', CategoryUpdateView.as_view()),
    path('todo/<int:pk>/delete/', TodoListDestroyView.as_view()),
    path('category/<int:pk>/delete/', CategoryDestroyView.as_view()),
    path('cache/', TotoAPIView.as_view())
]