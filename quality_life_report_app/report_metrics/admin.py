from django.contrib import admin
from .models import *

admin.site.site_header = 'Quality Life Report Database Admin'

admin.site.register(YouthIndex)
admin.site.register(AgingIndex)
admin.site.register(MonetaryPoverty)
admin.site.register(ExtremeMonetaryPoverty)
admin.site.register(SchoolEnrollment)
admin.site.register(DesertionRate)
admin.site.register(ViolentDeaths)
admin.site.register(FamilyViolence)
admin.site.register(VehicleRegistration)
admin.site.register(VehicleViolation)