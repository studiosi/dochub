from .models import Review, Task, TaskType, DoctorReview
from jsonview.views import JsonView
from django.db import transaction
from django.utils import timezone
from .taskExtra import create_tasks_plan

class ReviewCreateExtra(JsonView):

    @transaction.atomic
    def post(self, request):
        try:
            with transaction.atomic():
                # Create review
                r = Review(
                    name = request.POST['name'],
                    start_time = timezone.now,
                    end_time = None,
                    patient_id = request.POST['patient_id'],
                    comment = request.POST['comment'],
                    final_chosen_plan = None
                )
                review_id = r.save().id
                doctor_id = request.POST['doctor_id']
                # Create doctor review
                dr = DoctorReview(
                    doctor_id = doctor_id,
                    is_creator = True,
                    review_id = review_id,
                    chosen_plan_id = None
                )
                dr.save()
                # Create tasks
                te.create_tasks_plan(
                    doctor_id,
                    request.POST['plan_id'],
                    review_id
                )
                return { 'result' : 'OK' }
        except Exception:
            return { 'result' : 'ERR' }

class ReviewAddDoctorExtra(JsonView):

    @transaction.atomic
    def post(self, request):
        try:
            with transaction.atomic():                
                # Create doctor review
                doctor_id = request.POST['doctor_id']
                review_id = request.POST['review_id']
                dr = DoctorReview(
                    doctor_id = doctor_id,
                    is_creator = False,
                    review_id = review_id,
                    chosen_plan_id = None
                )
                dr.save()
                # Create tasks
                te.create_tasks_plan(
                    doctor_id,
                    request.POST['plan_id'],
                    review_id
                )
                return { 'result' : 'OK' }
        except Exception:
            return { 'result' : 'ERR' }