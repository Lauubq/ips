from django.utils import timezone
from django.contrib import admin
from .models import *

# Añadir las aplicaciones al panel de administración

class PatientAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'document_type', 'identity_card', 'nationality', 'full_name', 'first_name', 'second_name', 'surname',
        'second_surname', 'birthdate', 'sex', 'gender', 'occupation', 'opposition', 'wills', 'disability',
        'country_residence', 'city_residence', 'ethnic_belonging', 'territorial_zone', 'entity')
    list_filter = ('identity_card', 'first_name', 'second_name', 'surname', 'second_surname')
    search_fields = ['identity_card', 'first_name']
    readonly_field = ('uuid')
    fields = (
        'document_type', 'identity_card', 'first_name', 'second_name', 'surname', 'second_surname')
    ordering = ['document_type', 'identity_card', 'first_name', 'second_name', 'surname',
                'second_surname']

    # Sobrescribe el método save_model para agregar la fecha de creación y el usuario logueado
    #def save_model(self, request, obj, form, change):
     #   if not change:
      #      obj.date_created = timezone.now()
       #     obj.created_by = request.user
       # obj.date_update = timezone.now()
        #obj.updated_by = request.user
        #super().save_model(request, obj, form, change)



class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'uuid', 'date', 'modality', 'around', 'entry', 'cause',
        'triage', 'diagnosis')
    list_filter = ('uuid', 'modality', 'cause', 'diagnosis', 'triage')
    search_fields = ['uuid', 'modality']
    #readonly_fields = ('date_created', 'created_by', 'date_update', 'updated_by')
    fields = (
        'uuid', 'date', 'modality', 'around', 'entry', 'cause',
        'triage', 'diagnosis')
    ordering = ['uuid', 'date', 'modality', 'around', 'entry', 'cause',
        'triage', 'diagnosis']


class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = (
        'code', 'name')
    ordering = ['code']


class NacionalitiesAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    ordering = ['code']

class OccupationAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'father')
    ordering = ['code']

class OppositionAdmin(admin.ModelAdmin):
    list_display = ('code', 'manifest', 'date')
    ordering = ['code']

class WillsAdmin(admin.ModelAdmin):
    list_display = ('code', 'document', 'contact_service', 'date')
    ordering = ['code']

class DisabilityAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    ordering = ['code']

class Country_residenceAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    ordering = ['code']

class City_residenceAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    ordering = ['code']

class Ethnic_belongingAdmin(admin.ModelAdmin):
    list_display = ('code', 'ethnic', 'comunity')
    ordering = ['code']

class EntityAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    ordering = ['code']

admin.site.register(Patient, PatientAdmin)
admin.site.register(Contact_service, ContactAdmin)
admin.site.register(DocumentType, DocumentTypeAdmin)
admin.site.register(Nacionalities, NacionalitiesAdmin)
admin.site.register(Occupation, OccupationAdmin)
admin.site.register(Opposition, OppositionAdmin)
admin.site.register(Wills, WillsAdmin)
admin.site.register(Disability, DisabilityAdmin)
admin.site.register(Country_residence, Country_residenceAdmin)
admin.site.register(City_residence, City_residenceAdmin)
admin.site.register(Ethnic_belonging, Ethnic_belongingAdmin)
admin.site.register(Entity, EntityAdmin)
