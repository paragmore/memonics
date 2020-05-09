from django.contrib import admin
from .models import Post, PostImage, Comment, Like, Subject, Chapter


class PostImageInLine(admin.TabularInline):
    model = PostImage
    extra = 4


class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInLine]


admin.site.register(Post, PostAdmin)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Subject)
admin.site.register(Chapter)
