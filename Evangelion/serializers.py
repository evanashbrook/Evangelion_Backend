from rest_framework import serializers
from .models import App


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = (
            'title',
            'author',
            'date',
            'last_edit',
            'article',
        )