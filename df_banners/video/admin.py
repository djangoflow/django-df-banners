from typing import Any

from django.contrib import admin
from django.http import HttpRequest
from video_encoding.admin import FormatInline

from df_banners.video.models import BannerVideo


class BannerVideoInline(admin.TabularInline):
    model = BannerVideo
    extra = 0
    fields = ("video",)
    show_change_link = True


@admin.register(BannerVideo)
class BannerVideoAdmin(admin.ModelAdmin):
    inlines = [FormatInline]

    def get_model_perms(self, request: HttpRequest) -> Any:
        # Hide from admin index
        return {}
