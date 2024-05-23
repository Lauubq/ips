# Permite interactuar con la Base de Datos con el ORM de Django
# Las clases se convierten en tablas en la DB.
# Al modificar el código hay que hacer la migración para actualizar la DB.

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
import uuid


class DocumentType(models.Model):
    code = models.CharField(verbose_name = "Código", max_length = 3, primary_key = True)
    name = models.CharField(verbose_name = "Descripción", max_length = 50, unique = True, null = False)
    class Meta:
        db_table = 'document_type'
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documentos'
    def __str__(self):
        return f'{self.code} - {self.name}'


class Nacionalities(models.Model):
    code = models.CharField(verbose_name="Código", max_length=3, primary_key=True)
    name = models.CharField(verbose_name="Descripción", max_length=50, unique=True, null=False)
    class Meta:
        db_table = 'nacionalities'
        verbose_name = 'Nacionalidad'
        verbose_name_plural = 'Nacionalidades'
    def __str__(self):
        return f'{self.code} - {self.name}'


class Occupation(models.Model):
    code = models.CharField(verbose_name="Código", max_length=10, primary_key=True)
    name = models.CharField(verbose_name="Descripción", max_length=100, unique=True, null=False)
    father = models.ForeignKey("self", verbose_name = "Padre", on_delete = models.PROTECT, null=True) ##models.CASCADE
    class Meta:
        db_table = 'occupation'
        verbose_name = 'Ocupación'
        verbose_name_plural = 'Ocupaciones'
    def __str__(self):
        return f'{self.code} - {self.name} - {self.father}'


class Opposition(models.Model):
    code = models.AutoField(verbose_name="Código", primary_key=True)
    manifest = models.CharField(verbose_name="Manifestación", max_length=50, unique=True, null=False)
    date = models.DateTimeField(verbose_name="Fecha", max_length=50, unique=True, null=False )
    class Meta:
        db_table = 'opposition'
        verbose_name = 'Oposición'
        verbose_name_plural = 'Oposiciones'
    def __str__(self):
        return f'{self.code} - {self.manifest} - {self.date}'




class Disability(models.Model):
    code = models.CharField(verbose_name="Código", max_length=3, primary_key=True)
    name = models.CharField(verbose_name="Descripción", max_length=50, unique=True, null=False)
    class Meta:
        db_table = 'disability'
        verbose_name = 'Discapacidad'
        verbose_name_plural = 'Discapacidades'
    def __str__(self):
        return f'{self.code} - {self.name}'


class Country_residence(models.Model):
    code = models.CharField(verbose_name="Código", max_length=3, primary_key=True)
    name = models.CharField(verbose_name="Descripción", max_length=50, unique=True, null=False)
    class Meta:
        db_table = 'country_residence'
        verbose_name = 'País de recidencia'
        verbose_name_plural = 'Paises de recidencia'
    def __str__(self):
        return f'{self.code} - {self.name}'


class City_residence(models.Model):
    code = models.CharField(verbose_name="Código", max_length=10, primary_key=True)
    name = models.CharField(verbose_name="Descripción", max_length=50, unique=True, null=False)
    class Meta:
        db_table = 'city_residence'
        verbose_name = 'Ciudad de recidencia'
        verbose_name_plural = 'Ciudades de recidencia'
    def __str__(self):
        return f'{self.code} - {self.name}'



class Ethnic_belonging(models.Model):
    code = models.CharField(verbose_name="Código", max_length=3, primary_key=True)
    ethnic = models.CharField(verbose_name="Descripción", max_length=50, unique=True, null=False)
    comunity = models.CharField(verbose_name="Descripción", max_length=50, unique=True, null=False)
    class Meta:
        db_table = 'ethnic_belonging'
        verbose_name = 'Origen étnico'
        verbose_name_plural = 'Origenes étnicos'
    def __str__(self):
        return f'{self.code} - {self.ethnic} - {self.comunity}'



class Entity(models.Model):
    code = models.CharField(verbose_name="Código", max_length=10, primary_key=True)
    name = models.CharField(verbose_name="Descripción", max_length=200, unique=True, null=False)
    class Meta:
        db_table = 'entity'
        verbose_name = 'Entidad'
        verbose_name_plural = 'Entidades'
    def __str__(self):
        return f'{self.code} - {self.name}'

################################# Servicio de contacto ###############################################

class ShapeId(models.Model):
    code = models.CharField(verbose_name="Código", max_length=3, primary_key=True)
    name = models.CharField(verbose_name="Descripción", max_length=50, unique=True, null=False)
    class Meta:
        db_table = 'shape_id'
        verbose_name = 'Forma'
        verbose_name_plural = 'Formas'
    def __str__(self):
        return f'{self.code} - {self.name}'

class IdModality(models.Model):
    code = models.CharField(verbose_name="Código", max_length=3, primary_key=True)
    shape_id = models.ForeignKey(ShapeId, verbose_name = "Identidad de forma", on_delete = models.PROTECT) ##models.CASCADE
    service_group = models.CharField(verbose_name="Grupo de servicio", max_length=50, unique=True, null=False )
    class Meta:
        db_table = 'modalidad_ident'
        verbose_name = 'Modalidad de identidad'
        verbose_name_plural = 'Modalidades de identidades'
    def __str__(self):
        return f'{self.code} - {self.shape_id} - {self.service_group}'

class Entry(models.Model):
    code = models.CharField(verbose_name="Código", max_length=3, primary_key=True)
    name = models.CharField(verbose_name="descripción", max_length=100, unique=True, null=False )
    class Meta:
        db_table = 'entry'
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
    def __str__(self):
        return f'{self.code} - {self.name} '

class Cause(models.Model):
    code = models.CharField(verbose_name="Código", max_length=3, primary_key=True)
    name = models.CharField(verbose_name="descripción", max_length=200, unique=True, null=False )
    class Meta:
        db_table = 'Cause'
        verbose_name = 'Causa'
        verbose_name_plural = 'Causas'
    def __str__(self):
        return f'{self.code} - {self.name} '


class Triage(models.Model):
    code = models.CharField(verbose_name="Código", max_length=3, primary_key=True)
    category = models.CharField(verbose_name="Categoría", max_length=50, unique=True, null=False )
    date = models.DateTimeField(verbose_name="Fecha", max_length=50, unique=True, null=False )

    class Meta:
        db_table = 'triage'
        verbose_name = 'triage'
        verbose_name_plural = 'triages'
    def __str__(self):
        return f'{self.code} - {self.name} - {self.date}'


class Diagnosis(models.Model):
    code = models.CharField(verbose_name="Código", max_length=3, primary_key=True)
    name = models.CharField(verbose_name="descripción", max_length=50, unique=True, null=False )
    type = models.CharField(verbose_name="Tipo", max_length=50, unique=True, null=False )
    class Meta:
        db_table = 'diagnosis'
        verbose_name = 'Diagnóstico'
        verbose_name_plural = 'Diagnósticos'
    def __str__(self):
        return f'{self.code} - {self.name} - {self.type}'




class Contact_service(models.Model):
    uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    date = models.DateField('Fecha', editable=True)
    modality = models.ForeignKey(IdModality, verbose_name = 'Modalidad', null = False, on_delete = models.PROTECT)
    around = models.CharField('Primer Nombre', max_length = 60, null = False, blank = False)
    entry = models.ForeignKey(Entry, verbose_name = 'Entrada', null = False, on_delete = models.PROTECT)
    cause = models.ForeignKey(Cause, verbose_name = 'Causa', null = False, on_delete = models.PROTECT)
    triage = models.ForeignKey(Triage, verbose_name = 'triage', null = False, on_delete = models.PROTECT)
    diagnosis = models.ForeignKey(Diagnosis, verbose_name = 'Diagnóstico', null = False, on_delete = models.PROTECT)
    class Meta:
        db_table = 'contact_service'
        verbose_name = 'Servicio de contacto'
        verbose_name_plural = 'Servicios de contactos'


class Wills(models.Model):
    code = models.AutoField(verbose_name="Código", primary_key=True)
    document = models.CharField(verbose_name="codigo", max_length=3, unique=True, null=False )
    contact_service = models.ForeignKey(Contact_service, verbose_name="Codigo de prov", on_delete=models.PROTECT)  ##models.CASCADE
    date = models.DateTimeField(verbose_name="Fecha", max_length=50, unique=True, null=False )
    class Meta:
        db_table = 'wills'
        verbose_name = 'Documento de voluntad'
        verbose_name_plural = 'Documentos de voluntades'
    def __str__(self):
        return f'{self.document} - {self.contact_service} - {self.date}'


class Patient(models.Model):
    TYPE = [
        ('POL', 'Póliza de Salud'),
        ('PBS', 'Plan de Beneficios en Salud'),
        ('PAR', 'Particular'),
    ]

    uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    document_type = models.ForeignKey(DocumentType, verbose_name = "Tipo de Documento", on_delete = models.PROTECT)
    identity_card = models.CharField(verbose_name = 'Número de Identificación', max_length = 20)
    nationality = models.ForeignKey(Nacionalities, verbose_name = "nacionalidad", on_delete = models.PROTECT)
    full_name = models.CharField(verbose_name='Nombre Completo', max_length=250, null=True)
    first_name = models.CharField('Primer Nombre', max_length=60, null=False, blank=False)
    second_name = models.CharField('Segundo Nombre', max_length=60, null=True, blank=True)
    surname = models.CharField('Primer Apellido', max_length=60, null=False, blank=False)
    second_surname = models.CharField('Segundo Apellido', max_length=60, null=True, blank=True)
    birthdate = models.DateTimeField('Fecha de Nacimiento', null = False, blank = True)
    sex = models.CharField(verbose_name='Sexo', max_length=250, null=True)
    gender = models.CharField(verbose_name='Genero', max_length=250, null=True)
    occupation = models.ForeignKey(Occupation, verbose_name = "Ocupación", on_delete = models.PROTECT)
    opposition = models.ForeignKey(Opposition, verbose_name = "Oposición", on_delete = models.PROTECT)
    wills = models.ForeignKey(Wills, verbose_name = "Documento de voluntad", on_delete = models.PROTECT)
    disability = models.ForeignKey(Disability, verbose_name = "Discapacidad", on_delete = models.PROTECT)
    country_residence = models.ForeignKey(Country_residence, verbose_name = "País de recidencia", on_delete = models.PROTECT)
    city_residence = models.ForeignKey(City_residence, verbose_name = "Ciudad de recidencia", on_delete = models.PROTECT)
    ethnic_belonging = models.ForeignKey(Ethnic_belonging, verbose_name = "Origen étnico", on_delete = models.PROTECT)
    territorial_zone = models.CharField(verbose_name='Zona Territorial', max_length=250, null=True)
    entity = models.ForeignKey(Entity, verbose_name = "Entidad", on_delete = models.PROTECT)
    class Meta:
        db_table = 'patient'
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
        constraints = [
            models.UniqueConstraint(fields = ['document_type', 'identity_card'],
                                    name = 'UQ_DOCUMENT_TYPE_IDENTITY_CARD'),
        ]

    def __str__(self):
        return f'{self.document_type} - {self.identity_card} '.strip

    def second_surname_display(self):
        return self.second_surname if self.second_surname is not None else ''

    def second_name_display(self):
        return self.second_name if self.second_name is not None else ''

    def __str__(self):
        return f'{self.first_name} {self.second_name_display()} {self.surname} {self.second_surname_display()}'.strip()
