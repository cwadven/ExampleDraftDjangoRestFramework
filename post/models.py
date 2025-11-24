from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    guest_id = models.BigIntegerField(db_index=True)
    like_count = models.IntegerField(
        default=0,
        db_index=True,
    )
    comment_count = models.IntegerField(
        default=0,
        db_index=True,
    )
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} - {self.title}'
