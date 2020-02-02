from django.contrib import admin
from blog.models import Post, Tag, Comment


class AdminPost(admin.ModelAdmin):
    raw_id_fields = ('author', 'likes', 'tags')

class AdminTag(admin.ModelAdmin):
    pass

class AdminComment(admin.ModelAdmin):
    raw_id_fields = ('post', 'author')

admin.site.register(Post, AdminPost)
admin.site.register(Tag, AdminTag)
admin.site.register(Comment, AdminComment)
