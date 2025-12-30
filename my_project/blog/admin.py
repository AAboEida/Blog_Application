from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','publish','created','updated']
    list_filter = ['publish','created']
    search_fields = ['title']
    date_hierarchy = 'publish'
    raw_id_fields=['author']
    prepopulated_fields = {'slug':('title',)}
    ordering = ['publish','status']

    