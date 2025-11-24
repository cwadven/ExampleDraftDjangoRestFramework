from rest_framework import serializers

from post.services.get_post_services import get_post_liked


class PostGuestInformationSerializer(serializers.Serializer):
    guest_id = serializers.IntegerField()
    nickname = serializers.CharField()


class PostListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    guest_information = serializers.SerializerMethodField()
    like_count = serializers.IntegerField()
    comment_count = serializers.IntegerField()
    created_at = serializers.DateTimeField()

    def get_guest_information(self, obj):
        nickname_by_guest_id = self.context.get('nickname_by_guest_id')
        return PostGuestInformationSerializer(
            instance={
                'guest_id': obj.guest_id,
                'nickname': nickname_by_guest_id.get(obj.guest_id),
            },
        ).data


class PostDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(allow_blank=True)
    guest_information = serializers.SerializerMethodField()
    like_count = serializers.IntegerField()
    comment_count = serializers.IntegerField()
    is_liked = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    def get_guest_information(self, obj):
        nickname_by_guest_id = self.context.get('nickname_by_guest_id')
        return PostGuestInformationSerializer(
            instance={
                'guest_id': obj.guest_id,
                'nickname': nickname_by_guest_id.get(obj.guest_id),
            },
        ).data

    def get_is_liked(self, obj):
        requested_guest_id = self.context.get('requested_guest_id')
        if not requested_guest_id:
            return False
        return get_post_liked(requested_guest_id, obj.id)
