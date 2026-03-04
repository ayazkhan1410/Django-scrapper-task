from django.db import models
from django.contrib.auth.models import User


class Status(models.TextChoices):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    PENDING = 'pending'


class LogLevel(models.TextChoices):
    INFO = 'info'
    WARNING = 'warning'
    ERROR = 'error'


class Platform(models.TextChoices):
    WEB = 'web'
    TWITTER = 'twitter'
    YOUTUBE = 'youtube'
    INSTAGRAM = 'instagram'


class ScrapingTargetURL(models.Model):
    platform = models.CharField(max_length=20, choices=Platform.choices)
    url = models.URLField(unique=True)
    scraped_data_available = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Profile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='profiles'
    )
    target = models.ForeignKey(
        ScrapingTargetURL, on_delete=models.CASCADE,
        related_name='profiles'
    )
    status = models.CharField(
        max_length=20, choices=Status.choices,
        default=Status.PENDING
    )
    last_scraped_at = models.DateTimeField(null=True, blank=True)
    next_scrape_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'target')
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['target']),
            models.Index(fields=['status']),
        ]


class ProfileDataHistory(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE,
        related_name='data_history'
    )
    scraped_data = models.JSONField()
    scraped_at = models.DateTimeField(auto_now_add=True)


class ProfileLog(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE,
        related_name='logs'
    )
    level = models.CharField(
        max_length=10, choices=LogLevel.choices,
        default=LogLevel.INFO
    )
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
