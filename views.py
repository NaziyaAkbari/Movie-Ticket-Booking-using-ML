from django.shortcuts import render, redirect
from .models import Movie, Booking


def home(request):
    movies = Movie.objects.all()
    return render(request, 'booking/home.html', {'movies': movies})


def seats(request, id):
    movie = Movie.objects.get(id=id)
    booked = Booking.objects.filter(movie=movie).values_list('seat_number', flat=True)
    return render(request, 'booking/seats.html', {'movie': movie, 'booked': booked})


def book_ticket(request):
    if request.method == 'POST':
        movie_id = request.POST['movie_id']
        seat = request.POST['seat']
        name = request.POST['name']

        movie = Movie.objects.get(id=movie_id)

        Booking.objects.create(
            movie=movie,
            seat_number=seat,
            user_name=name
        )

        return render(request, 'booking/success.html')
def report(request):
    data = Booking.objects.all()
    return render(request, 'booking/report.html', {'data': data})    