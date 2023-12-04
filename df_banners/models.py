from df_cards.models import TitledCard
from django.db import models
from django.db.models import Count
from taggit.managers import TaggableManager


class BannerQuerySet(models.QuerySet):
    def filter_tags(self, tags: list[str]) -> models.QuerySet:
        return (
            self.filter(tags__name__in=tags)
            .annotate(num_tags=Count("tags"))
            .filter(num_tags=len(tags))
        )


class Banner(TitledCard, models.Model):
    objects = BannerQuerySet.as_manager()

    full_image = models.ImageField(upload_to="banners", blank=True, null=True)
    action_url = models.CharField(blank=True, default="", max_length=255)
    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ("sequence",)
