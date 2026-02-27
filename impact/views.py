from django.shortcuts import render
from .models import Division

def home(request):
    # Fetch all data from the database
    divisions = Division.objects.all()
    # Send it to the template
    return render(request, 'home.html', {'divisions': divisions})

def team(request):
    # This renders the Our Team page
    return render(request, 'team.html')

def partners(request):
    # This renders the Our Partners page
    return render(request, 'partners.html')

def media(request):
    # This renders the Media Gallery page
    return render(request, 'media.html')

