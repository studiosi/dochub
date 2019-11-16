from rest_framework import serializers
from .models import Doctor, Review, DoctorReview, Task, PlanComment

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

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('__all__')

class PlanCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanComment
        fields = ('__all__')