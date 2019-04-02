from rest_framework.serializers import ModelSerializer
from .models import Songs


class SongsSerializer(ModelSerializer):

    class Meta:
        model = Songs
        fields = ("title", "artist")

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.artist = validated_data.get("artist", instance.artist)
        instance.save()

        return instance