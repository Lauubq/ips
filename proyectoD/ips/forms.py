# Creacion de formularios

from django import forms

from .models import Medic, Patient


class MedicForm(forms.ModelForm):
    class Meta:
        model = Medic
        fields = [
            'document_type', 'identity_card', 'first_name',
            'second_name', 'surname', 'second_surname', 'cellphone',
            'professional_card'
        ]
        labels = {
            'document_type': 'Tipo Documento',
            'identity_card': 'Nro. Identificación',
            'first_name': 'Primer Nombre',
            'second_name': 'Segundo Nombre',
            'surname': 'Primer Apellido',
            'second_surname': 'Segundo Apellido',
            'cellphone': 'Nro. Celular',
            'professional_card': 'Nro. T. Profesional',
        }
        widgets = {
            'document_type': forms.Select(
                attrs = {
                    'class': 'form-select'
                }
            ),
            'identity_card': forms.NumberInput(
                attrs = {
                    'id': 'identity',
                    'class': 'form-control',
                    'placeholder': '1234567',
                }
            ),
            'first_name': forms.TextInput(
                attrs = {
                    'id': 'first.name',
                    'class': 'form-control',
                    'placeholder': 'Joe',
                }
            ),
            'second_name': forms.TextInput(
                attrs = {
                    'id': 'second.name',
                    'class': 'form-control',
                    'placeholder': 'Adam',
                }
            ),
            'surname': forms.TextInput(
                attrs = {
                    'id': 'surname',
                    'class': 'form-control',
                    'placeholder': 'Smith',
                }
            ),
            'second_surname': forms.TextInput(
                attrs = {
                    'id': 'second.surname',
                    'class': 'form-control',
                }
            ),
            'cellphone': forms.NumberInput(
                attrs = {
                    'id': 'cell',
                    'class': 'form-control',
                }
            )
            ,
            'professional_card': forms.NumberInput(
                attrs = {
                    'id': 'cell',
                    'class': 'form-control',
                }
            )
        }


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'document_type', 'identity_card', 'first_name',
            'second_name', 'surname', 'second_surname', 'full_name', 'birthday', 'sex',
            'gener', 'occupation', 'oposicion', 'wills_document', 'disability', 'country_residence', 'city_residence',
            'ethnic_belonging', 'territorial_zone', 'entity'
        ]
        labels = {
            'document_type': 'Tipo Documento',
            'identity_card': 'Nro. Identificación',
            'first_name': 'Primer Nombre',
            'second_name': 'Segundo Nombre',
            'surname': 'Primer Apellido',
            'second_surname': 'Segundo Apellido',
            'birthday': 'Fecha Nacimiento',
            'sex': 'Sexo',
            'gener': 'genero',
            'occupation': 'Ocupación',
            'oposicion': 'Oposición',
            'wills_document': 'Documento de voluntad',
            'disability': 'Discapacidad',
            'country_residence': 'País de recidencia',
            'city_residence': 'Ciudad de recidencia',
            'ethnic_belonging': 'Origen étnico',
            'territorial_zone': 'Zona Territorial',
            'entity': 'Entidad'

        }
        widgets = {
            'document_type': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'identity_card': forms.TextInput(
                attrs={
                    'id': 'identity',
                    'class': 'form-control',
                    'placeholder': '1234567',
                    'autocomplete': 'off'
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'id': 'first.name',
                    'class': 'form-control',
                    'placeholder': 'Joe',
                    'autocomplete': 'off'
                }
            ),
            'second_name': forms.TextInput(
                attrs={
                    'id': 'second.name',
                    'class': 'form-control',
                    'placeholder': 'Adam',
                    'autocomplete': 'off'
                }
            ),
            'surname': forms.TextInput(
                attrs={
                    'id': 'surname',
                    'class': 'form-control',
                    'placeholder': 'Smith',
                    'autocomplete': 'off'
                }
            ),
            'second_surname': forms.TextInput(
                attrs={
                    'id': 'second.surname',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'full_name': forms.TextInput(
                attrs={
                    'id': 'full.name',
                    'class': 'form-control',
                    'placeholder': 'Joe Adam Smith',
                    'autocomplete': 'off'
                }
            ),
            'birth_date': forms.DateTimeInput(
                attrs={
                    'id': 'birth.date',
                    'class': 'form-control',
                    'format': '%Y-%m-%d',
                    'type': 'date'
                }
            ),
            'sex': forms.Select(
                choices=[('Male', 'Male'), ('Female', 'Female')],
                attrs={
                    'class': 'form-select'
                }
            ),
            'gener': forms.TextInput(
                attrs={
                    'id': 'gener',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'occupation': forms.TextInput(
                attrs={
                    'id': 'occupation',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'oposicion': forms.TextInput(
                attrs={
                    'id': 'oposicion',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'wills_document': forms.TextInput(
                attrs={
                    'id': 'wills.document',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'disability': forms.TextInput(
                attrs={
                    'id': 'disability',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'country_residence': forms.TextInput(
                attrs={
                    'id': 'country.residence',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'city_residence': forms.TextInput(
                attrs={
                    'id': 'city.residence',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'ethnic_belonging': forms.TextInput(
                attrs={
                    'id': 'ethnic.belonging',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'territorial_zone': forms.TextInput(
                attrs={
                    'id': 'territorial.zone',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'entity': forms.TextInput(
                attrs={
                    'id': 'entity',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'cellphone': forms.NumberInput(
                attrs={
                    'id': 'cell',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'id': 'email',
                    'autocomplete': 'off',
                    'class': 'form-control',
                }
            ),
            'type': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
        }


class SearchPatient(forms.Form):
    filter = forms.CharField(label = "Filtrar por:")
