from django.db import models
from core.models import Profile


class TwitterProfile(models.Model):
    target_id = models.CharField(max_length=100)
    is_blue_verified = models.BooleanField(default=False)
    can_dm = models.BooleanField(default=False)
    default_profile = models.BooleanField(default=False)
    user_description = models.TextField()
    display_url = models.URLField(null=True, blank=True)
    expanded_url = models.URLField(null=True, blank=True)
    fast_followers_count = models.BigIntegerField(default=0)
    favourites_count = models.BigIntegerField()
    followers_count = models.BigIntegerField()
    friends_count = models.BigIntegerField()
    location = models.CharField(
        max_length=100, null=True, blank=True
    )
    media_count = models.BigIntegerField()
    target_name = models.CharField(max_length=100)
    normal_followers_count = models.BigIntegerField()
    screen_name = models.CharField(max_length=100)
    statuses_count = models.BigIntegerField()
    target_profile_created_at = models.DateTimeField()
    profile = models.ForeignKey(
        Profile, related_name='twitter_profiles',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TwitterTweet(models.Model):
    twitter_profile = models.ForeignKey(
        TwitterProfile, on_delete=models.CASCADE,
        related_name='twitter_tweets'
    )
    tweet_id = models.CharField(max_length=100)
    keywords = models.CharField(
        max_length=50, null=True, blank=True
    )
    tweet_text = models.CharField(max_length=280)
    clean_tweet_text = models.CharField(max_length=280)
    tweet_replies = models.BigIntegerField(default=0)
    tweet_quote_count = models.BigIntegerField(default=0)
    tweet_favorite_count = models.BigIntegerField(default=0)
    tweet_retweets = models.BigIntegerField(default=0)
    tweet_book_mark_count = models.BigIntegerField(default=0)
    tweet_likes = models.BigIntegerField(default=0)
    tweet_views = models.BigIntegerField()
    tweet_image_link = models.URLField(null=True, blank=True)
    tweet_video_link = models.URLField(null=True, blank=True)
    tweet_original_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
