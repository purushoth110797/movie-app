from django.core.management.base import BaseCommand
from movies.models import movie
import requests


class Command(BaseCommand):
    help = "Update movie data and get trailer links in the database"

    def handle(self, *args, **options):
        # Code to update the database with now playing movie data
        api_key = "a7768c78762e7d02a666812e3e1f306c"
        base_url = "https://api.themoviedb.org/3/movie/now_playing"
        page = 1

        params = {
            "api_key": api_key,
            "region": "IN",
        }

        all_movies = []

        while page <= 13:
            url = f'{base_url}?api_key={params["api_key"]}&region={params["region"]}&page={page}'
            response = requests.get(url)

            movie_data = response.json().get("results", [])

            all_movies.extend(movie_data)
            page += 1

        movie.objects.all().delete()

        for movie_data in all_movies:
            movie.objects.create(
                title=movie_data["title"],
                movieID=movie_data["id"],
                releaseDate=movie_data["release_date"],
                rating=movie_data["vote_average"],
                imageURL=movie_data["poster_path"],
                posterURL=movie_data["backdrop_path"],
                overview=movie_data["overview"],
            )

        self.stdout.write(self.style.SUCCESS("Now playing movie data updated."))

        # Code to get trailer links using movie IDs
        for movie_instance in movie.objects.all():
            movie_id = movie_instance.movieID
            trailer_link = self.get_movie_trailer_link(movie_id)
            movie_instance.trailer_link = trailer_link
            movie_instance.save()

        self.stdout.write(self.style.SUCCESS("Trailer links updated."))

    def get_movie_trailer_link(self, movie_id):
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos"
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhNzc2OGM3ODc2MmU3ZDAyYTY2NjgxMmUzZTFmMzA2YyIsInN1YiI6IjY1NTFkYWQ2NjdiNjEzNDVjZDMyYTRhMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.DZzagp4AOUucDdq2XOStPXKDD_elR9WxJsaSoDpMJXU",
        }
        response = requests.get(url, headers=headers)
        video_data = response.json().get("results", [])

        return self.first_trailer_link(video_data)

    def first_trailer_link(self, video_data):
        base_url = "https://www.youtube.com/watch?v="
        for video in video_data:
            if video["type"] == "Trailer":
                return base_url + video["key"]

        return None
