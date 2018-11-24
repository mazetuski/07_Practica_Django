from datetime import datetime

from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

    def create(self, validated_data):
        user = User()
        return self.update(user, validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance


class UserListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='blog', read_only=True)
    post_number = serializers.SerializerMethodField()

    def get_post_number(self, obj):
        return '{} posts'.format(obj.posts.filter(pub_date__lte=datetime.now()).count())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'url', 'post_number']
        read_only_fields = ['post_number']
