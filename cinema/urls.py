from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import genre_list, genre_detail, ActorList, ActorDetail, CinemaHallViewSet, MovieViewSet

router = DefaultRouter()
router.register('cinema-halls', CinemaHallViewSet, basename='cinema-hall')
router.register('movies', MovieViewSet, basename='movies')

urlpatterns = [
    path("genres/", genre_list, name="genre-list"),
    path("genres/<int:pk>/", genre_detail, name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path('', include(router.urls)),
]

app_name = "cinema"
