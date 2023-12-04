from celery import current_app as app
from video_encoding.tasks import convert_video

from df_banners.video.models import BannerVideo


@app.task(soft_time_limit=180, time_limit=200)
def process_video(pk: str) -> None:
    video = BannerVideo.objects.get(pk=pk)
    convert_video(video.video)
    video.create_thumbnail()
