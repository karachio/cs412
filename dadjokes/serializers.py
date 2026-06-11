from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Joke, Picture


class JokeSerializer(serializers.ModelSerializer):
    """
    Serializer for Joke model.
    """

    class Meta:
        model = Joke
        fields = ['id', 'text', 'contributor', 'timestamp']

    def create(self, validated_data):
        print(f'JokeSerializer.create, validated_data={validated_data}')


        return Joke.objects.create(**validated_data)


class PictureSerializer(serializers.ModelSerializer):
    """
    Serializer for Picture model.
    """

    class Meta:
        model = Picture
        fields = ['id', 'image_url', 'contributor', 'timestamp']

    def create(self, validated_data):
        print(f'PictureSerializer.create, validated_data={validated_data}')

        return Picture.objects.create(**validated_data)