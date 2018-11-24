from rest_framework import serializers

from blog.models import Post


class PostListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return '{} {}'.format(obj.owner.first_name, obj.owner.last_name)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description_short', 'url_assert', 'pub_date', 'user']


class PostSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return '{} {}'.format(obj.owner.first_name, obj.owner.last_name)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description_short', 'description_long', 'url_assert', 'pub_date', 'category', 'user']
        read_only_fields = ['user']

    def create(self, validated_data):
        post = Post()
        return self.update(post, validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title')
        instance.description_short = validated_data.get('description_short')
        instance.description_long = validated_data.get('description_long')
        instance.url_assert = validated_data.get('url_assert')
        instance.pub_date = validated_data.get('pub_date')
        instance.owner = self.context.get('request').user
        instance.save()
        instance.category.set(validated_data.get('category'))
        instance.save()
        return instance

