from core.consts import StrValueLabel


class MemberStatus(StrValueLabel):
    ACTIVE = ('ACTIVE', '활성')
    WITHDRAW = ('WITHDRAW', '탈퇴')
    BLOCK = ('BLOCK', '정지')


class MemberType(StrValueLabel):
    ADMIN = ('ADMIN', '관리자')
    MANAGER = ('MANAGER', '운영자')
    CLIENT = ('CLIENT', '사용자')


class MemberProvider(StrValueLabel):
    EMAIL = ('EMAIL', '오리지널 유저')
    KAKAO = ('KAKAO', '카카오')
    NAVER = ('NAVER', '네이버')
    GOOGLE = ('GOOGLE', '구글')
