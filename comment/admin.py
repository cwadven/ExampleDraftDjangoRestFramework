from django.contrib import admin

from comment.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'post_id',
        'content',
        'guest_id',
        'is_deleted',
        'created_at',
        'updated_at',
    ]


admin.site.register(Comment, CommentAdmin)
