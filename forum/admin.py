__author__ = 'jxl'
from django.contrib import admin
from forum.models import Category, Post



class EntryAdmin(admin.ModelAdmin):
    list_display = ('title','author','category','status','publish_at')
    search_fields = ('title','category')

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post, EntryAdmin)