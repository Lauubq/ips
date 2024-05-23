# Creacion de formularios

from django import forms

from .models import Contact_service, Patient


class Contact_serviceForm(forms.ModelForm):
    class Meta:
        model = Contact_service
        fields = [
            'date', 'modality', 'around', 'entry', 'cause', 'triage', 'diagnosis'
        ]
        labels = {
            'date': 'Fecha',
            'modality': 'Modalidad',
            'around': 'Entorno',
            'entry': 'Ingreso',
            'cause': 'Causa',
            'triage': 'Triage',
            'diagnosis': 'Diagnóstico'
        }
        widgets = {

            'modality': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'around': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Entorno de la atención',
                }
            ),
            'entry': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Via de Ingreso del usuario',
                }
            ),
            'cause': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Causa de la atención',
                }
            ),
            'triage': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Clasificación del triage',
                }
            ),
            'diagnosis': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Diagnóstico principal del ingreso',
                }
            ),
        }


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'document_type', 'identity_card', 'first_name',
            'second_name', 'surname', 'second_surname', 'full_name', 'birthdate', 'sex',
            'gender', 'occupation', 'opposition', 'wills', 'disability', 'country_residence', 'city_residence',
            'ethnic_belonging', 'territorial_zone', 'entity', 'nationality'
        ]
        labels = {
            'document_type': 'Tipo Documento',
            'identity_card': 'Nro. Identificación',
            'first_name': 'Primer Nombre',
            'second_name': 'Segundo Nombre',
            'surname': 'Primer Apellido',
            'second_surname': 'Segundo Apellido',
            'birthdate': 'Fecha Nacimiento',
            'sex': 'Sexo',
            'gender': 'genero',
            'occupation': 'Ocupación',
            'opposition': 'Oposición',
            'wills': 'Documento de voluntad',
            'disability': 'Discapacidad',
            'country_residence': 'País de recidencia',
            'city_residence': 'Ciudad de recidencia',
            'ethnic_belonging': 'Origen étnico',
            'territorial_zone': 'Zona Territorial',
            'entity': 'Entidad',
            'nationality': 'Nacionalidad'

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
            'birthdate': forms.DateTimeInput(
                attrs={
                    'id': 'birth.date',
                    'class': 'form-control',
                    'format': '%Y-%m-%d',
                    'type': 'date'
                }
            ),
            'sex': forms.Select(
                choices=[('H', 'Hombre'), ('M', 'Mujer'), ('I', 'Indeterminado/Intersexual')],
                attrs={
                    'class': 'form-select'
                }
            ),
            'gender': forms.Select(
                choices=[('M', 'Masculino'), ('F', 'Femenino'), ('T', 'Transgenero'), ('N', 'Neutro'), ('NA', 'No lo declara')],
                attrs={
                    'class': 'form-select'
                }
            ),
            'occupation': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'opposition': forms.Select(
                attrs={
                     'class': 'form-select'
                }
            ),
            'wills':forms.Select(
                attrs={
                     'class': 'form-select'
                }
            ),
            'disability': forms.Select(
                attrs={
                     'class': 'form-select'
                }
            ),
            'country_residence': forms.Select(
                attrs={
                     'class': 'form-select'
                }
            ),
            'city_residence': forms.Select(
                attrs={
                     'class': 'form-select'
                }
            ),
            'ethnic_belonging': forms.Select(
                attrs={
                     'class': 'form-select'
                }
            ),
            'territorial_zone': forms.Select(
                choices=[('U', 'Urbana'), ('R', 'Rural')],
                attrs={
                    'class': 'form-select'
                }
            ),
            'entity': forms.Select(
                attrs={
                     'class': 'form-select'
                }
            ),
            'nationality': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            )
        }


class SearchPatient(forms.Form):
    filter = forms.CharField(label = "Filtrar por:")
