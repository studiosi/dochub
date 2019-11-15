from django.views.decorators.http import require_http_methods 

@require_http_methods(["GET"])
def getDoctorList(request):
    pass

@require_http_methods(["GET", "DELETE"])
def manageDoctor(request):
    if request.method == "GET":
        # Get doctor
        pass
    if request.method == "DELETE":
        # Remove doctor
        pass
