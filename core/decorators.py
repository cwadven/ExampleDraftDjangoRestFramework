from functools import wraps
from typing import Callable, Any

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpRequest
from rest_framework.request import Request
from rest_framework.exceptions import APIException
from core.pagination import Pageable
from core.exceptions import CommonAPIException
from types import FunctionType


def with_pageable(
        default_size: int = 20,
        page_param: str = 'page',
        size_param: str = 'size',
) -> Callable:
    """
    - Supports: DRF APIView methods, Django class-based views, and function-based views.
    - The decorated function must accept a keyword argument named 'pageable'
      (e.g., def get(self, request, pageable) or def view(request, pageable)).
    """

    def _paging(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            request = kwargs.get('request')
            if request is None:
                request = next((x for x in args if isinstance(x, (WSGIRequest, HttpRequest, Request))), None)
            if request is None:
                raise CommonAPIException(
                    status_code=500,
                    error_summary='Not Request Callable',
                )

            try:
                if hasattr(request, 'query_params'):
                    params = request.query_params
                else:
                    params = getattr(request, 'GET', {})

                page = int(params.get(page_param, 1))
                size = int(params.get(size_param, default_size))
                page = max(1, page)
                size = max(1, size)
            except Exception as e:
                # Keep behavior simple per reference
                raise CommonAPIException(
                    status_code=500,
                    error_summary=str(e),
                )

            return func(
                *args,
                pageable=Pageable(
                    page=page,
                    size=size,
                ),
                **kwargs
            )

        return wrapper

    def decorator(cls_or_func: Any) -> Any:
        if isinstance(cls_or_func, FunctionType):
            return _paging(cls_or_func)
        # Class: only wrap common HTTP verb methods to avoid unintended wrapping
        for method_name in ('get', 'post', 'put', 'patch', 'delete'):
            if hasattr(cls_or_func, method_name):
                method = getattr(cls_or_func, method_name)
                if callable(method):
                    setattr(cls_or_func, method_name, _paging(method))
        return cls_or_func

    return decorator
