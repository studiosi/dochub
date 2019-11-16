from .models import Task, TaskType, Doctor, Review
from django.utils import timezone

def create_tasks_plan(doctor_id, plan_id, review_id):
    d = Doctor.objects.filter(pk=doctor_id)[0]
    r = Review.objects.filter(pk=review_id)[0]  
    for t_type in TaskType:
        t = Task(
            task_type = t_type,
            doctor_id = d,
            plan_id = plan_id,
            review_id = r,
            start_time = timezone.now(),
        )
        t.save()