from django.shortcuts import render
from .models import Owner, Patient
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def home(request):
    context = {'name': 'Djnagoer'}
    return render(request, 'base/home.html', context)


class OwnerList(ListView):
    model = Owner 
    template_name = 'base/owner_list.html'
    

class PatientList(ListView):
    model = Patient
    template_name = 'base/patient_list.html'
    

class OwnerCreate(CreateView):
    model = Owner
    template_name = 'base/owner_create_form.html'
    fields = ['first_name', 'last_name', 'phone']
    
    
class PatientCreate(CreateView):
    model = Patient
    template_name = 'base/patient_create_form.html'
    fields = ['animal_type', 'breed', 'pet_name', 'age', 'owner']
    

class OwnerUpdate(UpdateView):
    model = Owner
    template_name = 'base/owner_update_form.html'
    fields = ['first_name', 'last_name', 'phone']
    

class PatientUpdate(UpdateView):
    model = Patient 
    template_name = 'base/patient_update_form.html'
    fields = ['animal_type', 'breed', 'pet_name', 'age', 'owner']
    

class OwnerDelete(DeleteView):
    model = Owner
    template_name = 'base/owner_delete_form.html'
    

class PatientDelete(DeleteView):
    model = Patient
    template_name = 'base/owner_delete_form.html'