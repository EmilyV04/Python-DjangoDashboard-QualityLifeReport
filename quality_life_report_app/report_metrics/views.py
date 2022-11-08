from .models import *
from django.shortcuts import render, redirect

# VISTA DE INICIO
def index(request):
    return render(request, 'home.html')

# ---------------------------------------------------------------
# VISTA DE DEMOGRAFIA
def demography(request):
    youth_index = YouthIndex.objects.all
    aging_index = AgingIndex.objects.all
    context = {'youth_index': youth_index, 'aging_index': aging_index}
    return render(request, 'demography.html', context)
# ---------------------------------------------------------------
def create_youth(request):  
    if request.method == "POST":  
        youth_index_id = request.POST["id_juventud"]
        year = request.POST["anio"]
        city = request.POST["ciudad"]
        men_index = request.POST["ind_hom"]
        women_index = request.POST["ind_muj"]

        YouthIndex.objects.create(youth_index_id = youth_index_id, year = year, city = city, men_index = men_index, women_index = women_index)
        return redirect('/demography')
    else:  
        pass
def edit_youth_view(request,id):
    youth_index = YouthIndex.objects.get(youth_index_id=id) 
    return render(request, "demography.html", {"eyouth_index" : youth_index, "modal_youth_value" : '1'})
def edit_youth(request):
    if request.method == "POST":  
        ide = request.POST["eid_juventud"]
        year = request.POST["eanio"]
        city = request.POST["eciudad"]
        men_index = request.POST["eind_hom"]
        women_index = request.POST["eind_muj"]

        youth_index = YouthIndex.objects.get(youth_index_id = ide) 

        youth_index.youth_index_id = ide 
        youth_index.year = year
        youth_index.city = city
        youth_index.men_index = men_index
        youth_index.women_index = women_index

        youth_index.save()
        return redirect('/demography')
    else:  
        pass
def delete_youth(request, id):  
    youth_index = YouthIndex.objects.get(youth_index_id=id)  
    youth_index.delete()  
    return redirect('/demography')
# ---------------------------------------------------------------
def create_aging(request):  
    if request.method == "POST":  
        aging_index_id = request.POST["id_env"]
        year = request.POST["anio_env"]
        city = request.POST["ciudad_env"]
        men_index = request.POST["ind_hom_env"]
        women_index = request.POST["ind_muj_env"]

        AgingIndex.objects.create(aging_index_id = aging_index_id, year = year, city = city, men_index = men_index, women_index = women_index)
        return redirect('/demography')
    else:  
        pass
def edit_aging_view(request,id):
    aging_index = AgingIndex.objects.get(aging_index_id=id) 
    return render(request, "demography.html", {"eaging_index" : aging_index, "modal_aging_value" : '1'})
def edit_aging(request):
    if request.method == "POST":  
        ide = request.POST["eid_env"]
        year = request.POST["eanio_env"]
        city = request.POST["eciudad_env"]
        men_index = request.POST["eind_hom_env"]
        women_index = request.POST["eind_muj_env"]

        aging_index = AgingIndex.objects.get(aging_index_id = ide) 

        aging_index.aging_index_id = ide 
        aging_index.year = year
        aging_index.city = city
        aging_index.men_index = men_index
        aging_index.women_index = women_index

        aging_index.save()
        return redirect('/demography')
    else:  
        pass
def delete_aging(request, id):  
    aging_index = AgingIndex.objects.get(aging_index_id=id)  
    aging_index.delete()  
    return redirect('/demography')
# ---------------------------------------------------------------
# VISTA DE POBREZA
def poverty(request):
    monetary_poverty = MonetaryPoverty.objects.all
    extreme_monetary_poverty = ExtremeMonetaryPoverty.objects.all
    context = {'monetary_poverty': monetary_poverty, 'extreme_monetary_poverty': extreme_monetary_poverty}
    return render(request, 'poverty.html', context)
# ---------------------------------------------------------------
def create_pomo(request):  
    if request.method == "POST":  
        monetary_poverty_id = request.POST["id_pomo"]
        year = request.POST["anio_pomo"]
        city = request.POST["ciudad_pomo"]
        poverty_index = request.POST["ind_pover_pomo"]

        MonetaryPoverty.objects.create(monetary_poverty_id = monetary_poverty_id, year = year, city = city, poverty_index = poverty_index)
        return redirect('/poverty')
    else:  
        pass
def edit_pomo_view(request,id):
    monetary_poverty = MonetaryPoverty.objects.get(monetary_poverty_id=id) 
    return render(request, "poverty.html", {"emonetary_poverty" : monetary_poverty, "modal_pomo_value" : '1'})
def edit_pomo(request):
    if request.method == "POST":  
        ide = request.POST["eid_pomo"]
        year = request.POST["eanio_pomo"]
        city = request.POST["eciudad_pomo"]
        poverty_index = request.POST["eind_pover_pomo"]

        monetary_poverty = MonetaryPoverty.objects.get(monetary_poverty_id = ide) 

        monetary_poverty.monetary_poverty_id = ide 
        monetary_poverty.year = year
        monetary_poverty.city = city
        monetary_poverty.poverty_index = poverty_index

        monetary_poverty.save()
        return redirect('/poverty')
    else:  
        pass
def delete_pomo(request, id):  
    monetary_poverty = MonetaryPoverty.objects.get(monetary_poverty_id=id)  
    monetary_poverty.delete()  
    return redirect('/poverty')
# ---------------------------------------------------------------
def create_pomoex(request):  
    if request.method == "POST":  
        extreme_monetary_poverty_id = request.POST["id_pomoex"]
        year = request.POST["anio_pomoex"]
        city = request.POST["ciudad_pomoex"]
        poverty_index = request.POST["ind_pover_pomoex"]

        ExtremeMonetaryPoverty.objects.create(extreme_monetary_poverty_id = extreme_monetary_poverty_id, year = year, city = city, poverty_index = poverty_index)
        return redirect('/poverty')
    else:  
        pass
def edit_pomoex_view(request,id):
    extreme_monetary_poverty = ExtremeMonetaryPoverty.objects.get(extreme_monetary_poverty_id=id) 
    return render(request, "poverty.html", {"eextreme_monetary_poverty" : extreme_monetary_poverty, "modal_pomoex_value" : '1'})
def edit_pomoex(request):
    if request.method == "POST":  
        ide = request.POST["eid_pomoex"]
        year = request.POST["eanio_pomoex"]
        city = request.POST["eciudad_pomoex"]
        poverty_index = request.POST["eind_pover_pomoex"]

        extreme_monetary_poverty = ExtremeMonetaryPoverty.objects.get(extreme_monetary_poverty_id = ide) 

        extreme_monetary_poverty.extreme_monetary_poverty_id = ide 
        extreme_monetary_poverty.year = year
        extreme_monetary_poverty.city = city
        extreme_monetary_poverty.poverty_index = poverty_index

        extreme_monetary_poverty.save()
        return redirect('/poverty')
    else:  
        pass
def delete_pomoex(request, id):  
    extreme_monetary_poverty = ExtremeMonetaryPoverty.objects.get(extreme_monetary_poverty_id=id)  
    extreme_monetary_poverty.delete()  
    return redirect('/poverty')
# ---------------------------------------------------------------
# VISTA DE EDUCACION
def education(request):
    enrollment = SchoolEnrollment.objects.all
    desertion= DesertionRate.objects.all
    context = {'enrollment': enrollment, 'desertion': desertion}
    return render(request, 'education.html', context)
# ---------------------------------------------------------------
def create_enrollment(request):  
    if request.method == "POST":  
        enrollment_id = request.POST["id_enroll"]
        year = request.POST["anio_enroll"]
        educational_level = request.POST["level_enroll"]
        amount_enrollment_official = request.POST["enroll_of"]
        amount_enrollment_private = request.POST["enroll_pri"]

        SchoolEnrollment.objects.create(enrollment_id = enrollment_id, year = year, educational_level = educational_level, amount_enrollment_official = amount_enrollment_official, amount_enrollment_private = amount_enrollment_private)
        return redirect('/education')
    else:  
        pass
def edit_enrollment_view(request,id):
    enrollment = SchoolEnrollment.objects.get(enrollment_id=id) 
    return render(request, "education.html", {"eenrollment" : enrollment, "modal_enroll_value" : '1'})
def edit_enrollment(request):
    if request.method == "POST":  
        ide = request.POST["eid_enroll"]
        year = request.POST["eanio_enroll"]
        educational_level = request.POST["elevel_enroll"]
        amount_enrollment_official = request.POST["eenroll_of"]
        amount_enrollment_private = request.POST["eenroll_pri"]

        enrollment = SchoolEnrollment.objects.get(enrollment_id = ide) 

        enrollment.enrollment_id = ide 
        enrollment.year = year
        enrollment.educational_level = educational_level
        enrollment.amount_enrollment_official = amount_enrollment_official
        enrollment.amount_enrollment_private = amount_enrollment_private

        enrollment.save()
        return redirect('/education')
    else:  
        pass
def delete_enrollment(request, id):  
    enrollment = SchoolEnrollment.objects.get(enrollment_id=id)  
    enrollment.delete()  
    return redirect('/education')
# ---------------------------------------------------------------
def create_desertion(request):  
    if request.method == "POST":  
        desertion_id = request.POST["id_deser"]
        year = request.POST["anio_deser"]
        educational_level = request.POST["level_deser"]
        desertion_index = request.POST["deser_index"]

        DesertionRate.objects.create(desertion_id = desertion_id, year = year, educational_level = educational_level, desertion_index = desertion_index)
        return redirect('/education')
    else:  
        pass
def edit_desertion_view(request,id):
    desertion = DesertionRate.objects.get(desertion_id=id) 
    return render(request, "education.html", {"edesertion" : desertion, "modal_deser_value" : '1'})
def edit_desertion(request):
    if request.method == "POST":  
        ide = request.POST["eid_deser"]
        year = request.POST["eanio_deser"]
        educational_level = request.POST["elevel_deser"]
        desertion_index = request.POST["edeser_index"]

        desertion = DesertionRate.objects.get(desertion_id = ide) 

        desertion.desertion_id = ide 
        desertion.year = year
        desertion.educational_level = educational_level
        desertion.desertion_index = desertion_index

        desertion.save()
        return redirect('/education')
    else:  
        pass
def delete_desertion(request, id):  
    desertion = DesertionRate.objects.get(desertion_id=id)  
    desertion.delete()  
    return redirect('/education')
# ---------------------------------------------------------------
# VISTA DE SEGURIDAD
def safety(request):
    violent_death = ViolentDeaths.objects.all
    family_violence = FamilyViolence.objects.all
    context = {'violent_death': violent_death, 'family_violence': family_violence}
    return render(request, 'safety.html', context)
# ---------------------------------------------------------------
def create_death(request):  
    if request.method == "POST":  
        violent_death_id = request.POST["id_death"]
        year = request.POST["anio"]
        violent_death_amount = request.POST["amount"]
        suicide_index = request.POST["suicide"]
        accidental_deaths_index = request.POST["accident"]
        deaths_transportation_accidents_index = request.POST["transp"]
        homicidies_index = request.POST["homicide"]

        ViolentDeaths.objects.create(violent_death_id = violent_death_id, year = year, violent_death_amount = violent_death_amount, suicide_index = suicide_index, accidental_deaths_index = accidental_deaths_index, deaths_transportation_accidents_index = deaths_transportation_accidents_index, homicidies_index = homicidies_index)
        return redirect('/safety')
    else:  
        pass
def edit_death_view(request,id):
    death = ViolentDeaths.objects.get(violent_death_id=id) 
    return render(request, "safety.html", {"eviolent_death" : death, "modal_death_value" : '1'})
def edit_death(request):
    if request.method == "POST":  
        ide = request.POST["eid_death"]
        year = request.POST["eanio"]
        violent_death_amount = request.POST["eamount"]
        suicide_index = request.POST["esuicide"]
        accidental_deaths_index = request.POST["eaccident"]
        deaths_transportation_accidents_index = request.POST["etransp"]
        homicidies_index = request.POST["ehomicide"]

        death = ViolentDeaths.objects.get(violent_death_id = ide) 

        death.violent_death_id = ide 
        death.year = year
        death.violent_death_amount = violent_death_amount
        death.suicide_index = suicide_index
        death.accidental_deaths_index = accidental_deaths_index
        death.deaths_transportation_accidents_index = deaths_transportation_accidents_index
        death.homicidies_index = homicidies_index

        death.save()
        return redirect('/safety')
    else:  
        pass
def delete_death(request, id):  
    death = ViolentDeaths.objects.get(violent_death_id=id)  
    death.delete()  
    return redirect('/safety')
# ---------------------------------------------------------------
def create_family(request):  
    if request.method == "POST":  
        family_violence_id = request.POST["id_family"]
        year = request.POST["anio_fam"]
        family_violence_amount = request.POST["amount_fam"]
        older_adult_index = request.POST["adult"]
        children_teens_index = request.POST["child"]
        family_members_index = request.POST["fami"]
        partner_index = request.POST["pareja"]

        FamilyViolence.objects.create(family_violence_id = family_violence_id, year = year, family_violence_amount = family_violence_amount, older_adult_index = older_adult_index, children_teens_index = children_teens_index, family_members_index = family_members_index, partner_index = partner_index)
        return redirect('/safety')
    else:  
        pass
def edit_family_view(request,id):
    family = FamilyViolence.objects.get(family_violence_id=id) 
    return render(request, "safety.html", {"efamily_violence" : family, "modal_family_value" : '1'})
def edit_family(request):
    if request.method == "POST":  
        ide = request.POST["eid_family"]
        year = request.POST["eanio_fam"]
        family_violence_amount = request.POST["eamount_fam"]
        older_adult_index = request.POST["eadult"]
        children_teens_index = request.POST["echild"]
        family_members_index = request.POST["efami"]
        partner_index = request.POST["epareja"]

        family = FamilyViolence.objects.get(family_violence_id = ide) 

        family.family_violence_id = ide 
        family.year = year
        family.family_violence_amount = family_violence_amount
        family.older_adult_index = older_adult_index
        family.children_teens_index = children_teens_index
        family.family_members_index = family_members_index
        family.partner_index = partner_index

        family.save()
        return redirect('/safety')
    else:  
        pass
def delete_family(request, id):  
    family = FamilyViolence.objects.get(family_violence_id=id)  
    family.delete()  
    return redirect('/safety')
# ---------------------------------------------------------------
# VISTA DE MOVILIDAD
def mobility(request):
    vehicule_registration = VehicleRegistration.objects.all
    vehicule_violation = VehicleViolation.objects.all
    context = {'vehicule_registration': vehicule_registration, 'vehicule_violation': vehicule_violation}
    return render(request, 'mobility.html', context)
# ---------------------------------------------------------------
def create_matricula(request):  
    if request.method == "POST":  
        vehicule_registration_id = request.POST["id_matri"]
        year = request.POST["anio_matri"]
        auto_index = request.POST["auto_matri"]
        moto_index = request.POST["moto_matri"]
        others_index = request.POST["other_matri"]

        VehicleRegistration.objects.create(vehicule_registration_id = vehicule_registration_id, year = year, auto_index = auto_index, moto_index = moto_index, others_index = others_index)
        return redirect('/mobility')
    else:  
        pass
def edit_matricula_view(request,id):
    matricula = VehicleRegistration.objects.get(vehicule_registration_id=id) 
    return render(request, "mobility.html", {"evehicule_registration" : matricula, "modal_matricula_value" : '1'})
def edit_matricula(request):
    if request.method == "POST":  
        ide = request.POST["eid_matri"]
        year = request.POST["eanio_matri"]
        auto_index = request.POST["eauto_matri"]
        moto_index = request.POST["emoto_matri"]
        others_index = request.POST["eother_matri"]

        matricula = VehicleRegistration.objects.get(vehicule_registration_id = ide) 

        matricula.vehicule_registration_id = ide 
        matricula.year = year
        matricula.auto_index = auto_index
        matricula.moto_index = moto_index
        matricula.others_index = others_index

        matricula.save()
        return redirect('/mobility')
    else:  
        pass
def delete_matricula(request, id):  
    matricula = VehicleRegistration.objects.get(vehicule_registration_id=id)  
    matricula.delete()  
    return redirect('/mobility')
# ---------------------------------------------------------------
def create_comparendo(request):  
    if request.method == "POST":  
        vehicule_violation_id = request.POST["id_compa"]
        year = request.POST["anio_compa"]
        auto_index = request.POST["auto_compa"]
        moto_index = request.POST["moto_compa"]
        others_index = request.POST["other_compa"]

        VehicleViolation.objects.create(vehicule_violation_id = vehicule_violation_id, year = year, auto_index = auto_index, moto_index = moto_index, others_index = others_index)
        return redirect('/mobility')
    else:  
        pass
def edit_comparendo_view(request,id):
    comparendo = VehicleViolation.objects.get(vehicule_violation_id=id) 
    return render(request, "mobility.html", {"evehicule_violation" : comparendo, "modal_comparendo_value" : '1'})
def edit_comparendo(request):
    if request.method == "POST":  
        ide = request.POST["eid_compa"]
        year = request.POST["eanio_compa"]
        auto_index = request.POST["eauto_compa"]
        moto_index = request.POST["emoto_compa"]
        others_index = request.POST["eother_compa"]

        comparendo = VehicleViolation.objects.get(vehicule_violation_id = ide) 

        comparendo.vehicule_violation_id = ide 
        comparendo.year = year
        comparendo.auto_index = auto_index
        comparendo.moto_index = moto_index
        comparendo.others_index = others_index

        comparendo.save()
        return redirect('/mobility')
    else:  
        pass
def delete_comparendo(request, id):  
    comparendo = VehicleViolation.objects.get(vehicule_violation_id=id)  
    comparendo.delete()  
    return redirect('/mobility')