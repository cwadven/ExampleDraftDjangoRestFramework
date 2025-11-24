from core.exceptions import CommonAPIException


class PostNotFoundException(CommonAPIException):
    status_code = 404
    default_detail = '게시글을 찾지 못했습니다.'
    default_code = 'post-not-found'
