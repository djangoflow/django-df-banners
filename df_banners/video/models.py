import os

from django.contrib.contenttypes.fields import GenericRelation
from django.core.files import File
from django.db import models
from video_encoding.backends import get_backend
from video_encoding.models import Format
from video_encoding.utils import get_local_path

from df_banners.models import Banner


class BannerVideo(models.Model):
    banner = models.OneToOneField(
        Banner, on_delete=models.CASCADE, related_name="video"
    )
    video = models.FileField(upload_to="banners/videos")
    video_formats = GenericRelation(Format)

    def create_thumbnail(self, force: bool = False) -> None:
        if not self.video or (self.banner.full_image and not force):
            return

        encoding_backend = get_backend()

        with get_local_path(self.video) as source_path:
            thumbnail_path = encoding_backend.get_thumbnail(source_path)

            try:
                with open(thumbnail_path, "rb") as file_handler:
                    django_file = File(file_handler)
                    self.banner.full_image.save(
                        os.path.basename(thumbnail_path), django_file
                    )
                self.save()
            finally:
                os.unlink(thumbnail_path)
