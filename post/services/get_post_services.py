from django.db.models import QuerySet

from like.models import PostLike
from post.exceptions import PostNotFoundException
from post.models import Post
from core.pagination import (
    OffsetPage,
    Pageable,
    offset_paginate_queryset,
)


def get_active_posts() -> QuerySet[Post]:
    return Post.objects.filter(
        is_deleted=False,
    )


def get_active_posts_page(pageable: Pageable) -> OffsetPage[Post]:
    queryset = get_active_posts().order_by('-created_at')
    return offset_paginate_queryset(queryset, pageable)


def get_active_post(post_id: int) -> Post:
    try:
        return get_active_posts().get(id=post_id)
    except Post.DoesNotExist:
        raise PostNotFoundException()


def get_active_guest_post(guest_id: int, post_id: int) -> Post:
    try:
        return get_active_posts().get(
            guest_id=guest_id,
            id=post_id,
        )
    except Post.DoesNotExist:
        raise PostNotFoundException()


def get_post_liked(
        guest_id: int,
        post_id: int,
) -> bool:
    return PostLike.objects.filter(
        guest_id=guest_id,
        post_id=post_id,
    ).exists()
