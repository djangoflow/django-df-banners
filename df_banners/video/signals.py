from typing import Any

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from df_banners.video.models import BannerVideo
from df_banners.video.tasks import process_video


@receiver(post_save, sender=BannerVideo)
def clean_video_formats(sender: Any, instance: BannerVideo, **kwargs: Any) -> None:
    if not instance.video:
        instance.video_formats.all().delete()


@receiver(post_save, sender=BannerVideo)
def convert_video(sender, instance, **kwargs):  # type: ignore
    if instance.video:
        transaction.on_commit(lambda: process_video.delay(str(instance.pk)))
