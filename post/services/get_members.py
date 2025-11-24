from typing import (
    Dict,
    List,
    Optional,
    Set,
    Union,
)

from member.models import (
    Guest,
    Member,
)


def get_nickname_by_guest_id(
        guest_ids: Union[List[int], Set[int]]
) -> Dict[int, Optional[str]]:
    # Guest 쿼리
    guests = Guest.objects.filter(id__in=guest_ids)
    guest_by_id = {g.id: g for g in guests}

    # Member 쿼리 (member_id 가 None 인 것도 제외)
    member_ids = {g.member_id for g in guest_by_id.values() if g.member_id}
    members = Member.objects.filter(id__in=member_ids)
    member_by_id = {m.id: m for m in members}

    nickname_by_guest_id = {}

    for guest_id in guest_ids:
        guest = guest_by_id.get(guest_id)
        if not guest:
            # guest_id 가 잘못된 경우 fallback 처리
            nickname_by_guest_id[guest_id] = None
            continue

        member = member_by_id.get(guest.member_id)
        nickname_by_guest_id[guest_id] = (
            member.nickname if member else guest.temp_nickname
        )

    return nickname_by_guest_id
