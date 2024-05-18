from django.utils import timezone
from django.contrib import admin
from .models import Contact_service, DocumentType

# Añadir las aplicaciones al panel de administración

class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'document_type', 'id', 'nationality', 'first_name', 'second_name', 'surname',
        'second_surname', 'birthday', 'sex', 'gener', 'occupation', 'oposicion')
    list_filter = ('identity_card', 'professional_card', 'first_name', 'second_name', 'surname', 'second_surname')
    search_fields = ['identity_card', 'professional_card', 'first_name']
    readonly_fields = ('date_created', 'created_by', 'date_update', 'updated_by')
    fields = (
        'document_type', 'identity_card', 'first_name', 'second_name', 'surname', 'second_surname', 'professional_card',
        'cellphone')
    ordering = ['document_type', 'identity_card', 'professional_card', 'first_name', 'second_name', 'surname',
                'second_surname']

    # Sobrescribe el método save_model para agregar la fecha de creación y el usuario logueado
    def save_model(self, request, obj, form, change):
        if not change:
            obj.date_created = timezone.now()
            obj.created_by = request.user
        obj.date_update = timezone.now()
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)



class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'document_type', 'id', 'nationality', 'first_name', 'second_name', 'surname',
        'second_surname', 'birthday', 'sex', 'gener', 'occupation', 'oposicion')
    list_filter = ('identity_card', 'professional_card', 'first_name', 'second_name', 'surname', 'second_surname')
    search_fields = ['identity_card', 'professional_card', 'first_name']
    readonly_fields = ('date_created', 'created_by', 'date_update', 'updated_by')
    fields = (
        'document_type', 'identity_card', 'first_name', 'second_name', 'surname', 'second_surname', 'professional_card',
        'cellphone')
    ordering = ['document_type', 'identity_card', 'professional_card', 'first_name', 'second_name', 'surname',
                'second_surname']





class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = (
        'code', 'description')
    ordering = ['code']


admin.site.register(Contact_service, ContactAdmin)
admin.site.register(DocumentType, DocumentTypeAdmin)
