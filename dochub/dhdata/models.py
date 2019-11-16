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

class Task(models.Model):
    """A model of a task"""
    task_type = models.CharField(max_length=200)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
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
