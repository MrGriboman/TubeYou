from rest_framework.serializers import ModelSerializer

from .models import Videos, UserAccount

class VideoSerializer(ModelSerializer):
    class Meta:
        model = Videos
        fields = ['id', 'name', 'description', 'views', 'likes', 'dislikes', 'upload_time', 'preview',
                  'video', 'length', 'owner_id', 'avatar', 'author_name']

class UserAccountSerializer(ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['account_id', 'nickname', 'header', 'avatar', 'creation_time', 'description']
