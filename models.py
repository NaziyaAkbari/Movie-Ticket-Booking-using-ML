from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    user_name = models.CharField(max_length=100)
    
def __str__(self):
        return f"{self.user_name} - {self.movie.name} - {self.seat_number}"