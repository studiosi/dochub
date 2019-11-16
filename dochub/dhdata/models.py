from django.db import models

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
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    patient_id = models.IntegerField()
    comment = models.TextField()
    final_chosen_plan = models.IntegerField()

class DoctorReview(models.Model):
    """A model of relationship between doctor and reviewing case."""
    doctor_id = models.IntegerField()
    is_creator = models.BooleanField()
    review_id = models.IntegerField()
    chosen_plan_id = models.IntegerField()

class Task(models.Model):
    """A model of a task"""
    task_type = models.CharField(max_length=200)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    plan_id = models.IntegerField()
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class PlanComment(models.Model):
    """A model of a comment to a plan"""
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE)
    comment = models.TextField()
    plan_id = models.IntegerField()
