from typing import Any

from django.apps import apps
from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from django.db.models.query import QuerySet
from django.http import HttpRequest

from df_banners.models import Banner
from df_banners.video.tasks import process_video


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    search_fields = ("title", "sequence", "action_url", "tags__name")
    list_display = ("title", "sequence", "action_url", "tags_")

    def get_inlines(
        self, request: HttpRequest, obj: Any
    ) -> list[type[InlineModelAdmin]]:
        inlines = list(super().get_inlines(request, obj))
        if apps.is_installed("df_banners.video"):
            from df_banners.video.admin import BannerVideoInline

            inlines.append(BannerVideoInline)
        return inlines

    def tags_(self, obj: Banner) -> str:
        return ", ".join([t.name for t in obj.tags.all()])

    def process_video(self, request: HttpRequest, qs: QuerySet[Banner]) -> None:
        for banner in qs:
            process_video.delay(str(banner.video.pk))

    def get_actions(self, request: HttpRequest) -> Any:
        actions: Any = super().get_actions(request)
        if apps.is_installed("df_banners.video"):
            actions["process_video"] = (
                BannerAdmin.process_video,
                "process_video",
                "Process video",
            )
        return actions
