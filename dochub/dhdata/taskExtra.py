from .models import Task, TaskType, Doctor, Review
from django.utils import timezone
from braces.views import CsrfExemptMixin
from jsonview.views import JsonView
from .serializers import TaskSerializer

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

class ReviewCountTasksLeft(CsrfExemptMixin, JsonView):

    def get(self, request, review_id):
        try:
            c = Task.objects \
                    .filter(review_id=review_id) \
                    .filter(end_time__isnull=True) \
                    .count()
            return { 'result' : c }
        except Exception:
            return { 'result' : 'ERR' }

class GetDoctorRemainingTasks(CsrfExemptMixin, JsonView):

    def get(self, request, doctor_id):
        t = Task.objects.filter(end_time__isnull=True) \
                .filter(doctor_id=doctor_id)
        ts = TaskSerializer(t, many=True)
        return ts.data

