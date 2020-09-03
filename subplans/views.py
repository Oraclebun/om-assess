from django.shortcuts import render
from django.db.models import Q
from .models import PlanTitle, PlanType, PlanDetail

# Create your views here.


def index(request):

    # always true query:
    queries = ~Q(pk__in=[])
    
    # if a name is specified, add it to the query
    if ('query' in request.GET and request.GET['query']):
        plan_name = request.GET['query']
        queries = queries & Q(name__name__icontains=plan_name)

    if ('period' in request.GET and request.GET['period']):
        sub_period = int(request.GET['period'])
        queries = queries & Q(subscription_period__exact=sub_period)
    
    if (('query' or 'period') in request.GET):
        plan_details = PlanDetail.objects.filter(queries)
    else:
        #default plan
        plan_details = PlanDetail.objects.filter(Q(name__name__icontains='biodata & crm solution') & Q(subscription_period__exact=3))
    
    return render(request, 'subplans/index.template.html',{
        'plans': plan_details
    })
