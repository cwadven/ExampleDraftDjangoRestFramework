from django.contrib import admin

from like.models import (
    CommentLike,
    PostLike,
)


class PostLikeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'post_id',
        'guest_id',
        'is_deleted',
        'created_at',
        'updated_at',
    ]


class CommentLikeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'comment_id',
        'guest_id',
        'is_deleted',
        'created_at',
        'updated_at',
    ]


admin.site.register(PostLike, PostLikeAdmin)
admin.site.register(CommentLike, CommentLikeAdmin)
