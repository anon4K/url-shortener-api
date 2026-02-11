from django.contrib import admin
from .models import URL

@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    list_display = ['short_code', 'original_url', 'created_at', 'clicks']
    search_fields = ['short_code', 'original_url']
    readonly_fields = ['created_at', 'clicks']
# Register your models here.
