from django.db import models
from enum import Enum

class Doctor(models.Model):
    """A model of a doctor."""
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

    objects = models.Manager()

    def __str__(self):
        return f"Doctor: ID[{self.pk}] Name[{self.name}] Title[{self.title}]"

class Review(models.Model):
    """A model of a reviewing case."""
    name = models.CharField(max_length=200)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    patient_id = models.CharField(max_length=200)
    comment = models.TextField()
    final_chosen_plan = models.IntegerField(null=True)

    objects = models.Manager()

class DoctorReview(models.Model):
    """A model of relationship between doctor and reviewing case."""
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    is_creator = models.BooleanField()
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE)
    chosen_plan_id = models.IntegerField(null=True)

    objects = models.Manager()


class TaskType(Enum):
    REGION_CONTOUR_CHECK = 0,
    DOSE_DEVIATION_CHECK = 1,
    GEOMETRIES_DEVIATION_CHECK = 2,
    MONITOR_UNITS_CHECK = 3,
    DOSE_DISTRIBUTION_CHECK = 4,
    CRITICAL_ORGAN_METRICS_CHECK = 5,
    OPTIMALITY_CHECK = 6,
    ROBUSTNESS_CHECK = 7,
    SAFETY_CHECK = 8

class Task(models.Model):
    """A model of a task"""
    task_type = models.CharField(max_length=200)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="doctor_profile")
    helper_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="helper_doctor_profile", null=True)
    plan_id = models.IntegerField()
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    objects = models.Manager()

class PlanComment(models.Model):
    """A model of a comment to a plan"""
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE)
    comment = models.TextField()
    plan_id = models.IntegerField()

    objects = models.Manager()
