from django.shortcuts import render
from django.db.models import Q
from .models import PlanTitle, PlanType, PlanDetail

# Create your views here.


def index(request):
    print("now 1", request.GET)
    plan_details = PlanDetail.objects.all()
    # always true query:
    queries = ~Q(pk__in=[])
    # if a name is specified, add it to the query
    if ('query' in request.GET and request.GET['query']):
        plan_name = request.GET['query']
        queries = queries & Q(name__name__icontains=plan_name)

    if ('period' in request.GET and request.GET['period']):
        sub_period = request.GET['period']
        queries = queries & Q(subscription_period__exact=sub_period)
    
    plan_details = plan_details.filter(queries)
    print(plan_name)
    return render(request, 'subplans/index.template.html')
