from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DFVideosConfig(AppConfig):
    name = "df_banners.video"
    verbose_name = _("DjangoFlow Banners Video")
    default_auto_field = "hashid_field.BigHashidAutoField"

    def ready(self) -> None:
        try:
            import df_banners.video.signals  # noqa F401
        except ImportError:
            pass
