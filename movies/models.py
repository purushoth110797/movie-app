from django.db import models


# Create your models here.
class movie(models.Model):
    title = models.CharField(max_length=300)
    movieID = models.IntegerField()
    releaseDate = models.DateField()
    rating = models.FloatField()
    imageURL = models.URLField(null=True, blank=True)
    posterURL = models.URLField(null=True, blank=True)
    overview = models.TextField()
    # Add a field for storing the trailer link
    trailer_link = models.URLField(blank=True, null=True)

    # Declaring the name for each entries in the table
    def __str__(self):
        return self.title
