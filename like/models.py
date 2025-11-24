from django.db import models


class PostLike(models.Model):
    post_id = models.BigIntegerField(db_index=True)
    guest_id = models.BigIntegerField(db_index=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        db_index=True,
    )


class CommentLike(models.Model):
    comment_id = models.BigIntegerField(db_index=True)
    guest_id = models.BigIntegerField(db_index=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        db_index=True,
    )
