from .models import *
from django.shortcuts import render

# VISTA DE INICIO
def index(request):
    return render(request, 'home.html')

# VISTA DE DEMOGRAFIA
def demography(request):
    youth_index = YouthIndex.objects.all
    aging_index = AgingIndex.objects.all
    context = {'youth_index': youth_index, 'aging_index': aging_index}
    return render(request, 'demography.html', context)

# VISTA DE POBREZA
def poverty(request):
    monetary_poverty = MonetaryPoverty.objects.all
    extreme_monetary_poverty = ExtremeMonetaryPoverty.objects.all
    context = {'monetary_poverty': monetary_poverty, 'extreme_monetary_poverty': extreme_monetary_poverty}
    return render(request, 'poverty.html', context)

# VISTA DE EDUCACION
def education(request):
    enrollment = SchoolEnrollment.objects.all
    desertion= DesertionRate.objects.all
    context = {'enrollment': enrollment, 'desertion': desertion}
    return render(request, 'education.html', context)

# VISTA DE SEGURIDAD
def safety(request):
    violent_death = ViolentDeaths.objects.all
    family_violence = FamilyViolence.objects.all
    context = {'violent_death': violent_death, 'family_violence': family_violence}
    return render(request, 'safety.html', context)

# VISTA DE MOVILIDAD
def mobility(request):
    vehicule_registration = VehicleRegistration.objects.all
    vehicule_violation = VehicleViolation.objects.all
    context = {'vehicule_registration': vehicule_registration, 'vehicule_violation': vehicule_violation}
    return render(request, 'mobility.html', context)