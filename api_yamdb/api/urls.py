from django.urls import path, include
from rest_framework import routers

from .views import (
    SignUpViewSet, SignInViewSet, ReviewViewSet, CommentViewSet, GenreViewSet,
    CategoryViewSet, TitleViewSet, UserViewSet
)

app_name = 'api'

router = routers.DefaultRouter()
router.register('auth/signup', SignUpViewSet, basename='signups')
router.register('auth/token', SignInViewSet, basename='tokens')
router.register('users', UserViewSet, basename='users')
router.register(r'genres', GenreViewSet, basename='genres')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'titles', TitleViewSet, basename='titles')
router.register(
    r'titles/(?P<title_id>\d+?)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+?)/reviews/(?P<review_id>\d+?)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('', include(router.urls)),
]
