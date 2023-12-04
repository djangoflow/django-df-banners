import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.settings")

app = Celery("df-banners")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
