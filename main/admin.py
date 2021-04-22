from django.contrib import admin
from .models import Post,Comment
# # Register your models here.
# admin.site.register(Post)
# admin.site.register(Comment)

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline,]


admin.site.register(Post, ArticleAdmin)
admin.site.register(Comment)
