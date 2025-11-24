from post.models import Post


def create_post(
        guest_id: int,
        title: str,
        content: str,
) -> Post:
    return Post.objects.create(
        guest_id=guest_id,
        title=title,
        content=content,
    )
