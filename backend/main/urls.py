from django.urls import path, re_path, include

from .views import VideosViewSet, FindVideoSet, UserInfoAPIView, VideoAddAPIView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('mainvideos', VideosViewSet, basename='Videos')
router.register('findvideos', FindVideoSet, basename='FoundVideos')

urlpatterns = [
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('userinfo/', UserInfoAPIView.as_view()),
    path('addvideo/', VideoAddAPIView.as_view()),

] + router.urls