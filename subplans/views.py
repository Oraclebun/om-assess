from django.shortcuts import render, HttpResponse
from django.db.models import Q
from .models import PlanTitle, PlanType, PlanDetail
from django.http import JsonResponse

# Create your views here.


def index(request):
    plan_details = PlanDetail.objects.filter(
        Q(name__name__icontains='biodata & crm solution') &
        Q(subscription_period__exact=3))
    return render(request, 'subplans/index.template.html', {
        'plans': plan_details
    })


def changeplan(request):
    # if a name is specified, add it to the query
    # always true query:
    queries = ~Q(pk__in=[])
    if ('query' in request.GET and request.GET['query']):
        plan_name = request.GET['query']
        queries = queries & Q(name__name__iexact=plan_name)

    if ('period' in request.GET and request.GET['period']):
        sub_period = int(request.GET['period'])
        queries = queries & Q(subscription_period__exact=sub_period)

    if (('query' or 'period') in request.GET):
        plan_details = PlanDetail.objects.filter(queries)
    else:
        #default plan

        plan_details = PlanDetail.objects.filter(
            Q(name__name__icontains='biodata & crm solution') &
            Q(subscription_period__exact=3))

    plan_list = []
    for plan in plan_details:
        dictionary = {
            'name': plan.name.name,
            'plan_type': plan.plan_type.name,
            'subscription_period': plan.subscription_period,
            'savings': plan.savings,
            'price': plan.price,
            'biodata_no': plan.no_of_biodata,
            'emp_e_doc': plan.no_of_emp_e_doc,
            'subaccount': plan.no_of_subaccount,
            'subdomain': plan.no_of_subdomain_website,
            'enquiries': plan.no_sales_enquiries,
            'color_scheme': plan.color_scheme,
        }
        plan_list.append(dictionary)

    JSONobj = {}
    JSONobj['plans'] = plan_list

    return JsonResponse(JSONobj, safe=False)
