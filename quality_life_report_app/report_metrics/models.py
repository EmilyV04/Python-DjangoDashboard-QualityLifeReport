from django.db import models

# -------------- DEMOGRAFIA ---------------

# INDICE DE JUVENTUD
class YouthIndex(models.Model):
    youth_index_id = models.PositiveIntegerField(primary_key='true')
    year = models.IntegerField()
    city = models.CharField(max_length=255)
    men_index = models.DecimalField(max_length=5, max_digits=5, decimal_places=2)
    women_index = models.DecimalField(max_length=5, max_digits=5, decimal_places=2)

    # def __str__(self):
    #     return str(self.youth_index_id) + ' ' + self.city

# INDICE DE ENVEJECIMIENTO
class AgingIndex(models.Model):
    aging_index_id = models.PositiveIntegerField(primary_key='true')
    year = models.IntegerField()
    city = models.CharField(max_length=255)
    men_index = models.DecimalField(max_length=5, max_digits=5, decimal_places=2)
    women_index = models.DecimalField(max_length=5, max_digits=5, decimal_places=2)

    # def __str__(self):
    #     return str(self.aging_index_id) + ' ' + self.city

# -------------- POBREZA ---------------

# POBREZA MONETARIA
class MonetaryPoverty(models.Model):
    monetary_poverty_id = models.PositiveIntegerField(primary_key='true')
    year = models.IntegerField()
    city = models.CharField(max_length=255)
    poverty_index = models.DecimalField(max_length=5, max_digits=5, decimal_places=2)

# POBREZA MONETARIA EXTREMA
class ExtremeMonetaryPoverty(models.Model):
    extreme_monetary_poverty_id = models.PositiveIntegerField(primary_key='true')
    year = models.IntegerField()
    city = models.CharField(max_length=255)
    poverty_index = models.DecimalField(max_length=5, max_digits=5, decimal_places=2)

# -------------- EDUCACIÓN ---------------

# MATRICULA ESCOLAR POR NIVEL EDUCATIVO
class SchoolEnrollment(models.Model):
    TYPES = (
        ('MO', 'Matricula Oficial'),
        ('MP', 'Matricula Privada')
    )
    LEVELS = (
        ('m-prees', 'Preescolar'),
        ('m-bapri', 'Basica Primaria'),
        ('m-basecu', 'Basica Secundaria'),
        ('m-media', 'Media')
    )
    enrollment_id = models.PositiveIntegerField(primary_key='true')
    year = models.IntegerField()
    educational_level = models.CharField(max_length=256, choices=LEVELS)
    type_enrollment = models.CharField(max_length=256, choices=TYPES)
    amount_enrollment = models.IntegerField()

# TASA DE DESERCION
class DesertionRate(models.Model):
    LEVELS = (
        ('m-prees', 'Preescolar'),
        ('m-bapri', 'Basica Primaria'),
        ('m-basecu', 'Basica Secundaria'),
        ('m-media', 'Media')
    )
    desertion_id = models.PositiveIntegerField(primary_key='true')
    year = models.IntegerField()
    educational_level = models.CharField(max_length=256, choices=LEVELS)
    desertion_index = models.DecimalField(max_length=5, max_digits=5, decimal_places=2)

# -------------- SEGURIDAD ---------------

# MUERTES VIOLENTAS
class ViolentDeaths(models.Model):
    violent_death_id = models.PositiveIntegerField(primary_key='true')
    year = models.IntegerField()
    violent_death_amount = models.IntegerField()
    suicide_index = models.DecimalField(max_length=5, max_digits=5, decimal_places=2)
    accidental_deaths_index = models.DecimalField(max_length=5, max_digits=5, decimal_places=2)
    deaths_transportation_accidents_index = models.DecimalField(max_length=5, max_digits=5, decimal_places=2)
    homicidies_index = models.DecimalField(max_length=5, max_digits=5, decimal_places=2)

# VIOLENCIA INTRAFAMILIAR
class FamilyViolence(models.Model):
    family_violence_id = models.PositiveIntegerField(primary_key='true')
    year = models.IntegerField()
    family_violence_amount = models.IntegerField()
    older_adult_index = models.IntegerField()
    children_teens_index = models.IntegerField()
    family_members_index = models.IntegerField()
    partner_index = models.IntegerField()

# -------------- MOVILIDAD ---------------

# MATRICULA VEHICULAR
class VehicleRegistration(models.Model):
    TYPES = (
        ('t-auto', 'Automovil'),
        ('t-moto', 'Motocicleta'),
        ('t-otro', 'Otros')
    )
    vehicule_registration_id = models.PositiveIntegerField(primary_key='true')
    year = models.IntegerField()
    vehicule_type = models.CharField(max_length=256, choices=TYPES)
    vehicule_registration_index = models.IntegerField()

# COMPARENDOS
class VehicleViolation(models.Model):
    TYPES = (
        ('t-auto', 'Automovil'),
        ('t-moto', 'Motocicleta'),
        ('t-otro', 'Otros')
    )
    vehicule_violation_id = models.PositiveIntegerField(primary_key='true')
    year = models.IntegerField()
    vehicule_type = models.CharField(max_length=256, choices=TYPES)
    vehicule_violation_index = models.IntegerField()
