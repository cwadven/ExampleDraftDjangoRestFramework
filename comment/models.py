from django.db import models


class Comment(models.Model):
    post_id = models.BigIntegerField(db_index=True)
    content = models.TextField()
    guest_id = models.BigIntegerField(db_index=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} {self.post_id}'
