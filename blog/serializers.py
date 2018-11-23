from rest_framework import serializers

from blog.models import Post


class PostCountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'