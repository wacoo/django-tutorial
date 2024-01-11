from django.shortcuts import render
from .models import Machine
# Create your views here.
def home(request):
    machines = Machine.objects.all()
    return render(request, 'index.html', {'machines': machines})