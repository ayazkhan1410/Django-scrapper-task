from django.db import models
from core.models import Profile


class YoutubeChannel(models.Model):
    channel_name = models.CharField(max_length=255)
    subscriber_count = models.BigIntegerField(default=0)
    videos_count = models.BigIntegerField(default=0)
    views = models.BigIntegerField(default=0)
    country = models.CharField(max_length=100)
    join_date = models.DateTimeField()
    description = models.TextField()
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE,
        related_name='youtube_channels'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class YoutubeVideo(models.Model):
    title = models.CharField(max_length=255)
    upload_date = models.DateTimeField()
    image = models.URLField()
    video_duration = models.PositiveIntegerField(default=0)
    description = models.TextField()
    views_count = models.BigIntegerField(default=0)
    like_count = models.BigIntegerField(default=0)
    comment_count = models.BigIntegerField(default=0)
    transcript_language = models.CharField(
        max_length=100, null=True, blank=True
    )
    transcript = models.TextField(null=True, blank=True)
    youtube_channel = models.ForeignKey(
        YoutubeChannel, on_delete=models.CASCADE,
        related_name='youtube_videos'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
