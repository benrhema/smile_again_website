from django.shortcuts import render
from .models import Division

def home(request):
    # Fetch all data from the database
    divisions = Division.objects.all()
    # Send it to the template
    return render(request, 'home.html', {'divisions': divisions})