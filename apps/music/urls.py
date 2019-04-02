from django.urls import path,include

from rest_framework.routers import DefaultRouter
from .views import ListCreateSongsView, SongsDetailView

router = DefaultRouter()

router.register('songs', ListCreateSongsView)


urlpatterns = [
    path('songs/', ListCreateSongsView.as_view(), name="songs-list-create"),
]