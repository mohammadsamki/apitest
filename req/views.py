from django.shortcuts import render
from rest_framework import generics
from .serializers import SnipteSerializer
from .models import Snipte
# Create your views here.


def index(request):
    return render(request, 'index.html')


class GetSnipte(generics.ListAPIView):
    queryset = Snipte.objects.all()
    serializer_class = SnipteSerializer
