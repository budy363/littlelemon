from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Booking
from .serializers import BookingSerializer

class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


from datetime import datetime

def home(request):
    return render(request, 'index.html', {
        'current_year': datetime.now().year
    })
