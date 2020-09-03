from django.db import models

# Create your models here.


class PlanTitle(models.Model):
    name = models.CharField(blank=False, max_length=80)

    def __str__(self):
        return self.name


class PlanType(models.Model):
    name = models.CharField(blank=False, max_length=10)

    def __str__(self):
        return self.name


class PlanDetail(models.Model):
    name = models.ForeignKey(PlanTitle, on_delete=models.CASCADE)
    plan_type = models.ForeignKey(PlanType, on_delete=models.CASCADE)
    subscription_period = models.IntegerField(blank=False, 
                                              null=False, default=3)
    savings = models.DecimalField(max_digits=2, decimal_places=0,
                                  blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=3,
                                blank=False)
    no_of_biodata = models.IntegerField(blank=True, null=True)
    no_of_emp_e_doc = models.IntegerField(blank=True, null=True)
    no_of_subaccount = models.IntegerField(blank=False, null=False)
    no_of_subdomain_website = models.IntegerField(blank=False, null=False, default=1)
    no_sales_enquiries = models.CharField(blank=True, max_length=20)
    color_scheme = models.CharField(blank=False, max_length=20)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name.name},{self.plan_type.name}'
