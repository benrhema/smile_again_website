from django.contrib import admin
from .models import (
    Division, TeamMember, Partner, GalleryItem, 
    HomeSettings, SiteValue, Testimonial, Event, 
    NewsArticle, DonationSubmission
)

@admin.register(HomeSettings)
class HomeSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not HomeSettings.objects.exists()

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role_title', 'category')
    list_filter = ('category',)

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

@admin.register(GalleryItem)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'is_featured')

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'is_published')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'summary')

# Using the decorator for consistency
@admin.register(SiteValue)
class SiteValueAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')

admin.site.register(Testimonial)
admin.site.register(Event)

@admin.register(DonationSubmission)
class DonationSubmissionAdmin(admin.ModelAdmin):
    # Added 'phone' here so you can see it immediately in the dashboard
    list_display = ('submitted_at', 'first_name', 'last_name', 'amount', 'phone', 'donation_type')
    list_filter = ('donation_type', 'submitted_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    readonly_fields = ('submitted_at',)
    ordering = ('-submitted_at',)