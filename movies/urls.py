from django.urls import path
from . import views

# urls for this app
urlpatterns = [
    path("", views.home, name="movie_list"),
    path("movie_detail/<int:id>", views.movie_detail, name="movie_detail"),
    path("update_movies/", views.update_movies, name="update_movies"),
]
