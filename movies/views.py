from django.core.management import call_command
from django.shortcuts import render, redirect
from .models import movie
from django.core.paginator import Paginator
import requests


# Create your views here.
def home(request):
    movies = movie.objects.all()
    paginator = Paginator(movies, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    return render(
        request=request, template_name="home.html", context={"movies": page_obj}
    )


# detail view
def movie_detail(request, id):
    movie_instance = movie.objects.get(id=id)
    return render(request, "movie_detail.html", {"movie": movie_instance})


def update_movies(request):
    # Trigger the update_movies command
    call_command("update_movies")

    # Redirect to the movie list page or any other page you want to display after updating
    return redirect("movie_list")
