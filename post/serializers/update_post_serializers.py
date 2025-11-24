from rest_framework import serializers


class UpdatePostSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField(max_length=None)

    def validate_title(self, value):
        if len(value) >= 50:
            raise serializers.ValidationError('최대 글자는 50개 입니다.')
        return value


class UpdatePostResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
