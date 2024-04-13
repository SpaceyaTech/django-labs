from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Category)

@admin.action(description="Mark selected stories as published")
def make_published(modeladmin, request, queryset):
    queryset.update(status="p")

@admin.action(description="Mark selected stories as withdrawn")
def make_withdrawn(modeladmin, request, queryset):
    queryset.update(status="w")

@admin.action(description="Mark selected stories as published")
def make_draft(modeladmin, request, queryset):
    queryset.update(status="d")

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', )
    actions = [make_published, make_withdrawn,make_draft]

