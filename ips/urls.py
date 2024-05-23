from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    #path('', index, name = "index"),
    path('', Index.as_view(), name = "index"),
    path('patient/', FilterPatients, name = 'patients'),
    path('patient/add',  CreatePatient,name = 'create_patient'),
    path('patient/edit/<str:uuid>',  EditPatient,name = 'edit_patient'),
    path('patient/delete/<str:uuid>',  DeletePatient,name = 'delete_patient'),
    path('contact/',  ContactList.as_view(),name = 'contact'),
    path('contact/add',  CreateContact.as_view(),name = 'create_contact'),
    path('contact/edit/<str:pk>', UpdateContact.as_view(), name = 'update_contact'),
    path('contact/delete/<str:pk>',DeleteContact.as_view(),name = 'delete_contact'),
]

