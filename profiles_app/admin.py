from django.contrib import admin

from .models import UserProfile, ProfileFeedItem


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'last_login',)

class ProfileFeedItemAdmin:
    list_display = ('user_profile', 'created_on',)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ProfileFeedItem)