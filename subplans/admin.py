from django.contrib import admin
from .models import PlanTitle, PlanType, PlanDetail

# Register your models here.
admin.site.register(PlanTitle)
admin.site.register(PlanType)
admin.site.register(PlanDetail)