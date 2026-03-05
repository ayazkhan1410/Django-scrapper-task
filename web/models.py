from django.db import models
from core.models import Profile


class WebSource(models.Model):
    host_name = models.CharField(max_length=255)
    source_hostname = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class WebArticle(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=255, null=True, blank=True)
    web_source = models.ForeignKey(
        WebSource, on_delete=models.CASCADE,
        related_name='web_articles'
    )
    date = models.DateField(null=True, blank=True)
    fingerprint = models.CharField(max_length=100, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    raw_text = models.TextField()
    text = models.TextField()
    language = models.CharField(max_length=10, null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    page_type = models.CharField(max_length=50, null=True, blank=True)
    file_date = models.DateField(null=True, blank=True)
    excerpt = models.CharField(max_length=100, null=True, blank=True)
    tags = models.CharField(max_length=100, null=True, blank=True)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE,
        related_name='web_articles'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
