from post.models import Post
from post.services.get_post_services import get_active_guest_post


def update_post(
        guest_id: int,
        post_id: int,
        title: str,
        content: str,
) -> Post:
    post = get_active_guest_post(
        guest_id=guest_id,  # request.guest.id 같이 설정
        post_id=post_id,
    )
    post.title = title
    post.content = content
    post.save(
        update_fields=[
            'title',
            'content',
            'updated_at',
        ],
    )
    return post
