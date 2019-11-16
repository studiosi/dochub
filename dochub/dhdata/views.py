from django.shortcuts import render
from rest_framework import viewsets
from .models import Doctor, Review, DoctorReview, Task, PlanComment
from .serializers import DoctorSerializer, ReviewSerializer, DoctorReviewSerializer, TaskSerializer, PlanCommentSerializer

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

class TaskReviewViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all() 
    serializer_class = TaskSerializer

class PlanCommentReviewViewSet(viewsets.ModelViewSet):
    queryset = PlanComment.objects.all() 
    serializer_class = PlanCommentSerializer