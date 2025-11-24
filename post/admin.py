from django.contrib import admin

from post.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'content',
        'guest_id',
        'like_count',
        'comment_count',
        'is_deleted',
        'created_at',
        'updated_at',
    ]


admin.site.register(Post, PostAdmin)
