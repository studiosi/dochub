from django.contrib import admin

from .models import Doctor, DoctorReview, Task, Review, PlanComment

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    pass

@admin.register(DoctorReview)
class DoctorReviewAdmin(admin.ModelAdmin):
    pass

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

@admin.register(PlanComment)
class PlanCommentAdmin(admin.ModelAdmin):
    pass