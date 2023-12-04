from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DFBannersConfig(AppConfig):
    name = "df_banners"
    verbose_name = _("DjangoFlow Banners")
    default_auto_field = "hashid_field.BigHashidAutoField"

    class DFMeta:
        api_path = "banners/"
