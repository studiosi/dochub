from rest_framework import serializers
from .models import Doctor,Review, DoctorReview

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ["id","name","title"]

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ["id","name","start_time","end_time","patient_id","comment","final_chosen_plan"]

class DoctorReviewSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = DoctorReview
        fields = ('__all__')