from typing import Any

from django.apps import apps
from drf_spectacular.utils import extend_schema_field
from hashid_field.rest import HashidSerializerCharField
from rest_framework import serializers

from ..models import Banner


class VideoFormatSerializer(serializers.Serializer):
    format = serializers.CharField()
    progress = serializers.IntegerField(required=False)
    file = serializers.FileField(required=False)
    width = serializers.IntegerField(required=False)
    height = serializers.IntegerField(required=False)


class VideoSerializer(serializers.Serializer):
    video = serializers.FileField(required=False)
    video_formats = VideoFormatSerializer(many=True, required=False)


class BannerSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField(read_only=True)
    tags = serializers.SerializerMethodField()
    video = serializers.SerializerMethodField(allow_null=True)

    @extend_schema_field(VideoSerializer)
    def get_video(self, obj: Any) -> Any:
        if apps.is_installed("df_banners.video"):
            try:
                return VideoSerializer(obj.video).data
            except Banner.video.RelatedObjectDoesNotExist:
                return None

        return None

    def get_tags(self, obj: Any) -> list[str]:
        return [tag.slug for tag in obj.tags.all()]

    class Meta:
        model = Banner
        fields = [
            "id",
            "title",
            "tags",
            "description",
            "full_image",
            "action_url",
            "sequence",
            "video",
        ]
