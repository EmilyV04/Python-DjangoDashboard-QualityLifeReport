"""quality_life_report_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path
from report_metrics import views as v

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^home/', v.index, name='home'),
    # ---------------------------------------------------------------
    re_path(r'^demography/', v.demography, name='demography'),
    re_path(r'^create_youth', v.create_youth, name='create_youth'),
    path('delete_youth/<int:id>', v.delete_youth, name='delete_youth'),
    path('edit_youth_view/<int:id>', v.edit_youth_view, name='edit_youth_view'),
    path('edit_youth', v.edit_youth, name='edit_youth'),
    re_path(r'^create_aging', v.create_aging, name='create_aging'),
    path('delete_aging/<int:id>', v.delete_aging, name='delete_aging'),
    path('edit_aging_view/<int:id>', v.edit_aging_view, name='edit_aging_view'),
    path('edit_aging', v.edit_aging, name='edit_aging'),
    # ---------------------------------------------------------------
    re_path(r'^poverty/', v.poverty, name='poverty'),
    re_path(r'^create_pomo', v.create_pomo, name='create_pomo'),
    path('delete_pomo/<int:id>', v.delete_pomo, name='delete_pomo'),
    path('edit_pomo_view/<int:id>', v.edit_pomo_view, name='edit_pomo_view'),
    path('edit_pomo', v.edit_pomo, name='edit_pomo'),
    re_path(r'^create_pomoex', v.create_pomoex, name='create_pomoex'),
    path('delete_pomoex/<int:id>', v.delete_pomoex, name='delete_pomoex'),
    path('edit_pomoex_view/<int:id>', v.edit_pomoex_view, name='edit_pomoex_view'),
    path('edit_pomoex', v.edit_pomoex, name='edit_pomoex'),
    # ---------------------------------------------------------------
    re_path(r'^education/', v.education, name='education'),
    re_path(r'^create_enrollment', v.create_enrollment, name='create_enrollment'),
    path('delete_enrollment/<int:id>', v.delete_enrollment, name='delete_enrollment'),
    path('edit_enrollment_view/<int:id>', v.edit_enrollment_view, name='edit_enrollment_view'),
    path('edit_enrollment', v.edit_enrollment, name='edit_enrollment'),
    re_path(r'^create_desertion', v.create_desertion, name='create_desertion'),
    path('delete_desertion/<int:id>', v.delete_desertion, name='delete_desertion'),
    path('edit_desertion_view/<int:id>', v.edit_desertion_view, name='edit_desertion_view'),
    path('edit_desertion', v.edit_desertion, name='edit_desertion'),
    # ---------------------------------------------------------------
    re_path(r'^safety/', v.safety, name='safety'),
    re_path(r'^create_death', v.create_death, name='create_death'),
    path('delete_death/<int:id>', v.delete_death, name='delete_death'),
    path('edit_death_view/<int:id>', v.edit_death_view, name='edit_death_view'),
    path('edit_death', v.edit_death, name='edit_death'),
    re_path(r'^create_family', v.create_family, name='create_family'),
    path('delete_family/<int:id>', v.delete_family, name='delete_family'),
    path('edit_family_view/<int:id>', v.edit_family_view, name='edit_family_view'),
    path('edit_family', v.edit_family, name='edit_family'),
    # ---------------------------------------------------------------
    re_path(r'^mobility/', v.mobility, name='mobility'),
    re_path(r'^create_matricula', v.create_matricula, name='create_matricula'),
    path('delete_matricula/<int:id>', v.delete_matricula, name='delete_matricula'),
    path('edit_matricula_view/<int:id>', v.edit_matricula_view, name='edit_matricula_view'),
    path('edit_matricula', v.edit_matricula, name='edit_matricula'),
    re_path(r'^create_comparendo', v.create_comparendo, name='create_comparendo'),
    path('delete_comparendo/<int:id>', v.delete_comparendo, name='delete_comparendo'),
    path('edit_comparendo_view/<int:id>', v.edit_comparendo_view, name='edit_comparendo_view'),
    path('edit_comparendo', v.edit_comparendo, name='edit_comparendo'),
]

admin.site.site_url = '/home'
