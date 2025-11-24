from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from post.serializers.create_post_serializers import (
    CreatePostResponseSerializer,
    CreatePostSerializer,
)
from post.serializers.get_post_serializers import (
    PostDetailSerializer,
    PostListSerializer,
)
from post.serializers.update_post_serializers import (
    UpdatePostResponseSerializer,
    UpdatePostSerializer,
)
from post.services.create_post_services import create_post
from post.services.get_members import get_nickname_by_guest_id
from post.services.get_post_services import (
    get_active_post,
    get_active_posts, get_active_guest_post,
)
from post.services.update_post_services import update_post


class PostListView(APIView):
    def post(self, request):
        # Input Serializer
        create_post_serializer = CreatePostSerializer(data=request.data)
        create_post_serializer.is_valid(raise_exception=True)

        # Service Layer
        post = create_post(
            guest_id=1,  # request.guest.id 같이 설정
            title=create_post_serializer.validated_data['title'],
            content=create_post_serializer.validated_data['content'],
        )

        # Output Serializer
        return Response(
            CreatePostResponseSerializer(
                instance=post
            ).data,
            status=status.HTTP_201_CREATED,
        )

    def get(self, request):
        # Input Serializer
        # Service Layer
        posts = get_active_posts().order_by('-created_at')
        # Output Serializer
        return Response(
            PostListSerializer(
                posts,
                many=True,
                context={
                    'nickname_by_guest_id': get_nickname_by_guest_id(
                        {post.guest_id for post in posts}
                    ),
                    'requested_guest_id': None,
                }
            ).data,
            status=status.HTTP_200_OK,
        )


class PostDetailAPIView(APIView):
    def put(self, request, post_id: int):
        # Input Serializer
        update_post_serializer = UpdatePostSerializer(data=request.data)
        update_post_serializer.is_valid(raise_exception=True)

        # Service Layer
        post = update_post(
            guest_id=1,
            post_id=post_id,
            title=update_post_serializer.validated_data['title'],
            content=update_post_serializer.validated_data['content'],
        )

        # Output Serializer
        return Response(
            UpdatePostResponseSerializer(
                instance=post
            ).data,
            status=status.HTTP_200_OK,
        )

    def get(self, request, post_id: int):
        # Input Serializer
        # Service Layer
        post = get_active_post(post_id)
        # Output Serializer
        return Response(
            PostDetailSerializer(
                instance=post,
                context={
                    'nickname_by_guest_id': get_nickname_by_guest_id([post.guest_id]),
                    'requested_guest_id': None,
                }
            ).data,
            status=status.HTTP_200_OK,
        )
