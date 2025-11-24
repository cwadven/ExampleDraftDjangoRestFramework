from typing import (
    Dict,
    List,
)

from rest_framework.exceptions import APIException


class CommonAPIException(APIException):
    status_code = 500
    default_detail = '예상치 못한 에러가 발생했습니다.'
    default_code = 'unexpected-error'

    def __init__(
            self,
            status_code: int = None,
            error_summary: str = None,
            error_code: str = None,
            errors: Dict[str, List[str]] = None
    ):
        if status_code:
            self.status_code = status_code
        if error_summary:
            self.default_detail = error_summary
        if error_code:
            self.default_code = error_code
        self.errors = errors
        self.detail = self.default_detail
