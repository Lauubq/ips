from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    #path('', index, name = "index"),
    path('', Index.as_view(), name = "index"),
    path('patient/', login_required(FilterPatients), name = 'patients'),
    path('patient/add', login_required(CreatePatient), name = 'create_patient'),
    path('patient/edit/<str:uuid>', login_required(EditPatient), name = 'edit_patient'),
    path('patient/delete/<str:uuid>', login_required(DeletePatient), name = 'delete_patient'),
    path('contact/', login_required(ContactList.as_view()), name = 'contact'),
    path('contact/add', login_required(CreateContact.as_view()), name = 'create_contact'),
    path('contact/edit/<str:pk>', login_required(UpdateContact.as_view()), name = 'update_contact'),
    path('contact/delete/<str:pk>', login_required(DeleteContact.as_view()), name = 'delete_contact'),
]

