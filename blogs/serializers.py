from rest_framework import serializers
from .models import BlogsModel,CommentModel


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=CommentModel
        fields='__all__'


class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = BlogsModel
        fields = '__all__'