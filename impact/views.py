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
    stats = {
        'corp': Partner.objects.filter(category='CORPORATE').count(),
        'ngo': Partner.objects.filter(category='NGO').count(),
        'govt': Partner.objects.filter(category='GOVT').count(),
    }
    return render(request, 'partners.html', {'partners': partners, 'stats': stats})

def media(request):
    # Fetch videos and photos separately for organized sections
    video_items = GalleryItem.objects.filter(media_type='VIDEO').order_by('-created_at')
    photo_items = GalleryItem.objects.filter(media_type='PHOTO').order_by('-created_at')
    
    # We still keep the featured item option
    featured = GalleryItem.objects.filter(is_featured=True).first()

    context = {
        'videos': video_items,
        'photos': photo_items,
        'featured': featured,
    }
    return render(request, 'media.html', context)