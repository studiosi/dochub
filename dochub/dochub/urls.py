"""dochub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from dhdata import views
from dhdata import reviewExtra, taskExtra

router = routers.DefaultRouter()
router.register(r'doctors', views.DoctorViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'doctorreview', views.DoctorReviewViewSet)
router.register(r'tasks', views.TaskReviewViewSet)
router.register(r'plancomment', views.PlanCommentViewSet)


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # REST API URLs
    path('', include(router.urls)),
    # REVIEW
    path('reviews/create', reviewExtra.ReviewCreateExtra.as_view()),
    path('reviews/doctor', reviewExtra.ReviewAddDoctorExtra.as_view()),
    path('reviews/doctor/<int:doctor_id>', reviewExtra.GetDoctorReviews.as_view()),
    path('reviews/check/<int:review_id>', taskExtra.ReviewCountTasksLeft.as_view()),
    path('tasks/doctor/<int:doctor_id>', taskExtra.GetDoctorRemainingTasks.as_view()),
    path('tasks/review/<int:review_id>', reviewExtra.GetReviewTasks.as_view())

]   

