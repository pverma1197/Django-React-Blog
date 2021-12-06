from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class BlogSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = ('uuid', 'heading', 'article', 'image', 'user', 'tags')


class GetBlogSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Blog
        fields = ('uuid', 'heading', 'article', 'image', 'user', 'tags')


class BlogListSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Blog
        fields = ('heading', 'article', 'image', 'tags')


class BlogViewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Blog
        fields = ('heading', 'article', 'image', 'tags', 'user')
