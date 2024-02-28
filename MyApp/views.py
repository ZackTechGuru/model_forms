from django.shortcuts import render
from MyApp.forms import StudentForm

def home(request):
    Stud=StudentForm
    return render(request, 'index.html', {'form': Stud})

# Create your views here.
