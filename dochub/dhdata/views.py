from django.shortcuts import render
from rest_framework import viewsets
from .models import Doctor, Review, DoctorReview
from .serializers import DoctorSerializer, ReviewSerializer, DoctorReviewSerializer

# Create your views here.
class DoctorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class DoctorReviewViewSet(viewsets.ModelViewSet):
    queryset = DoctorReview.objects.all() 
    serializer_class = DoctorReviewSerializer