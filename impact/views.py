from django.shortcuts import render
from .models import Division, TeamMember, Partner, GalleryItem

def home(request):
    divisions = Division.objects.all().order_by('order')
    return render(request, 'home.html', {'divisions': divisions})

def team(request):
    leadership = TeamMember.objects.filter(category='LEADERSHIP')
    staff = TeamMember.objects.filter(category='CORE')
    return render(request, 'team.html', {'leadership': leadership, 'staff': staff})

def partners(request):
    partners = Partner.objects.all()
    # You can also send counts to make those yellow boxes dynamic!
    stats = {
        'corp': Partner.objects.filter(category='CORPORATE').count(),
        'ngo': Partner.objects.filter(category='NGO').count(),
        'govt': Partner.objects.filter(category='GOVT').count(),
    }
    return render(request, 'partners.html', {'partners': partners, 'stats': stats})

def media(request):
    featured = GalleryItem.objects.filter(is_featured=True).first()
    items = GalleryItem.objects.filter(is_featured=False).order_by('-created_at')
    return render(request, 'media.html', {'featured': featured, 'items': items})