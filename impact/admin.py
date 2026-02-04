from django.contrib import admin

# Register your models here.
from .models import Division

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('title', 'goal_amount')
