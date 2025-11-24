from django.conf import settings
from django.contrib import admin
from django.urls import (
    include,
    path,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('member', include('member.urls')),
    path('post', include('post.urls')),
    path('comment', include('comment.urls')),
    path('like', include('like.urls')),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]