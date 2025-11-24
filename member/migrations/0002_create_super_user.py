from datetime import datetime

from django.db import migrations

from member.consts import (
    MemberProvider,
    MemberStatus,
    MemberType,
)


def forward(apps, schema_editor):
    Member = apps.get_model('member', 'Member')
    member = Member.objects.create_superuser(
        username='admin',
        email='admin@admin.com',
        password='admin1q2w3e4r!',
    )
    member.member_type = MemberType.ADMIN.value
    member.member_status = MemberStatus.ACTIVE.value
    member.member_provider = MemberProvider.EMAIL.value
    member.first_name = '관'
    member.last_name = '리자'
    member.nickname = 'admin'
    member.last_login = datetime.now()
    member.save()

    Guest = apps.get_model('member', 'Guest')
    Guest.objects.get_or_create(
        ip='000.000.000.000',
        temp_nickname='관리자',
        member_id=member.id,
    )


def backward(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forward, backward)
    ]
