from .models import Review, Task, TaskType, DoctorReview
from jsonview.views import JsonView
from django.db import transaction
from django.utils import timezone
from .taskExtra import create_tasks_plan
from braces.views import CsrfExemptMixin
from .models import Doctor, Review

class ReviewCreateExtra(CsrfExemptMixin, JsonView):

    @transaction.atomic    
    def post(self, request):
        try:
            with transaction.atomic():
                # Create review
                r = Review(
                    name = request.POST['name'],
                    start_time = timezone.now(),
                    patient_id = request.POST['patient_id'],
                    comment = request.POST['comment']
                )
                r.save()
                review_id = r.pk
                doctor_id = request.POST['doctor_id']
                # Create doctor review
                dr = DoctorReview(
                    doctor_id = Doctor.objects.filter(pk=doctor_id)[0],
                    is_creator = True,
                    review_id = Review.objects.filter(pk=review_id)[0],
                )
                dr.save()
                # Create tasks
                create_tasks_plan(
                    doctor_id,
                    request.POST['plan_id'],
                    review_id
                )
                return { 'result' : 'OK' }
        except Exception:
            return { 'result' : 'ERR' }

class ReviewAddDoctorExtra(CsrfExemptMixin, JsonView):

    @transaction.atomic
    def post(self, request):
        try:
            with transaction.atomic():                
                # Create doctor review
                doctor_id = request.POST['doctor_id']
                d = Doctor.objects.filter(pk=doctor_id)[0]
                review_id = request.POST['review_id']
                r = Review.objects.filter(pk=review_id)[0]
                dr = DoctorReview(
                    doctor_id = d,
                    is_creator = False,
                    review_id = r,
                )
                dr.save()
                # Create tasks
                create_tasks_plan(
                    doctor_id,
                    request.POST['plan_id'],
                    review_id
                )
                return { 'result' : 'OK' }
        except Exception:
            return { 'result' : 'ERR' }