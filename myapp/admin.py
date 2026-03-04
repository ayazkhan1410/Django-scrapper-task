from django.contrib import admin
from .models import ScrapingTargetURL, Profile, ProfileDataHistory, ProfileLog


@admin.register(ScrapingTargetURL)
class ScrapingTargetURLAdmin(admin.ModelAdmin):
    list_display = (
        'url', 'platform',
        'scraped_data_available', 'created_at'
    )
    list_filter = ('platform', 'scraped_data_available')
    search_fields = ('url',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'target', 'status',
        'last_scraped_at', 'created_at'
    )
    list_filter = ('status',)
    search_fields = ('user__username', 'target__url', 'target__username')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(ProfileDataHistory)
class ProfileDataHistoryAdmin(admin.ModelAdmin):
    list_display = ('profile', 'scraped_at')
    search_fields = ('profile__user__username', 'profile__target__url')
    readonly_fields = ('scraped_at',)


@admin.register(ProfileLog)
class ProfileLogAdmin(admin.ModelAdmin):
    list_display = ('profile', 'level', 'message', 'created_at')
    list_filter = ('level',)
    search_fields = ('profile__user__username', 'message')
    readonly_fields = ('created_at',)
