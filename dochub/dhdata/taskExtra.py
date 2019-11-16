from .models import Task, TaskType
from django.utils import timezone

def create_tasks_plan(doctor_id, plan_id, review_id):
    for t_type in TaskType:
        t = Task(
            task_type = t_type,
            doctor_id = doctor_id,
            helper_id = None,
            plan_id = plan_id,
            review_id = review_id,
            start_time = timezone.now(),
            end_time = None,
        )
        t.save()