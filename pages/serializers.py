from email.policy import default
from django.forms import fields
from rest_framework import serializers
from .models import TodoList,Category
from django.utils import timezone


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('id', 'title', 'content', 'category')


class TodoListDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'


class TodoListCreateSerializer(serializers.ModelSerializer):
    created = serializers.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = serializers.DateField(default=timezone.now().strftime("%Y-%m-%d"))

    class Meta:
        model = TodoList
        fields = ('id', 'title', 'content', 'created', 'due_date', 'category')

        