from django.contrib import admin
from .models import (
    Target, Profile,
    ScrapLog
)


@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'url', 'platform', 'created_at'
    )
    list_filter = ('platform',)
    search_fields = ('url',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'target', 'status',
        'last_scraped_at', 'created_at'
    )
    list_filter = ('status',)
    search_fields = ('user__username', 'target__url', 'target__username')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(ScrapLog)
class ScrapLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'level', 'message', 'created_at')
    list_filter = ('level',)
    search_fields = ('profile__user__username', 'message')
    readonly_fields = ('created_at',)
