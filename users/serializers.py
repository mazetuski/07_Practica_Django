from datetime import datetime

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

    def encrypt_password(self, validated_data):
        password = validated_data.get('password')
        if password:
            validated_data['password'] = make_password(password)

    def create(self, validated_data):
        self.encrypt_password(validated_data)
        user = super().create(validated_data)
        return user

    def update(self, instance, validated_data):
        self.encrypt_password(validated_data)
        user = super().update(instance, validated_data)
        return user


class UserListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='blog', read_only=True)
    post_number = serializers.SerializerMethodField()

    def get_post_number(self, obj):
        return '{} posts'.format(obj.posts.filter(pub_date__lte=datetime.now()).count())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'url', 'post_number']
        read_only_fields = ['post_number']
