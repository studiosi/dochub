from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from dhdata.models import Doctor

@require_http_methods(["GET"])
def getDoctorList(request):
    qs = Doctor.objects.all()
    qs_json = serializers.serialize('json', qs)
    return HttpResponse(qs_json, content_type='application/json')

@require_http_methods(["GET", "DELETE"])
@csrf_exempt
def manageDoctor(request, doctorid):
    if request.method == "GET":
        # Read doctor
        qs = Doctor.objects.filter(pk__exact=doctorid)
        qs_json = serializers.serialize('json', qs)
        return HttpResponse(qs_json, content_type='application/json')
    if request.method == "DELETE":
        # Remove doctor
        qs = Doctor.objects.filter(pk__exact=doctorid).delete()
        if qs[0] == 0:
            data = {"result" : "NOK"}
            return JsonResponse(data)
        else:
            data = {"result" : "OK"}
            return JsonResponse(data, safe=False)
