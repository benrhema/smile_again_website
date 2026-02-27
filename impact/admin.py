from django.contrib import admin
from .models import Division, TeamMember, Partner, GalleryItem

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