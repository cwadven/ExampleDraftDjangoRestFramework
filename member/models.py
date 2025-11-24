from django.contrib.auth.models import AbstractUser
from django.db import models

from member.consts import (
    MemberProvider,
    MemberStatus,
    MemberType,
)


class Member(AbstractUser):
    nickname = models.CharField(
        max_length=256,
        db_index=True,
        unique=True,
    )
    member_type = models.CharField(
        max_length=50,
        choices=MemberType.choices()
    )
    member_status = models.CharField(
        max_length=50,
        choices=MemberStatus.choices()
    )
    member_provider = models.CharField(
        max_length=50,
        choices=MemberProvider.choices()
    )
    profile_image_url = models.TextField()

    class Meta:
        verbose_name = '일반 사용자'
        verbose_name_plural = '일반 사용자'


class Guest(models.Model):
    ip = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        db_index=True,
    )
    temp_nickname = models.CharField(
        max_length=256,
        db_index=True,
        unique=True,
    )
    member_id = models.BigIntegerField(
        blank=True,
        null=True,
        db_index=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
