from django.contrib import admin

from member.models import (
    Guest,
    Member,
)


class GuestAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'ip',
        'temp_nickname',
        'member_id',
        'created_at',
    ]


class MemberAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nickname',
        'member_type',
        'member_status',
        'member_provider',
    ]


admin.site.register(Guest, GuestAdmin)
admin.site.register(Member, MemberAdmin)
