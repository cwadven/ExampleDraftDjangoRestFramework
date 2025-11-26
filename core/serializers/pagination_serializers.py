from rest_framework import serializers


class PaginationSerializer(serializers.Serializer):
    current_page = serializers.IntegerField()
    size = serializers.IntegerField()
    total_count = serializers.IntegerField()
    has_next = serializers.BooleanField()
    has_prev = serializers.BooleanField()
