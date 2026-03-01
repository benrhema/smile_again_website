from django.shortcuts import render, redirect
from .models import (
    Division, TeamMember, Partner, GalleryItem, 
    HomeSettings, SiteValue, Testimonial, Event, 
    NewsArticle, DonationSubmission
)

def home(request):
    settings = HomeSettings.objects.first()
    values = SiteValue.objects.all().order_by('order')
    divisions = Division.objects.all().order_by('order')
    testimonials = Testimonial.objects.all()
    events = Event.objects.all().order_by('date')
    featured_event = Event.objects.filter(is_featured=True).first()
    
    # Fetch the latest 2 published articles
    news = NewsArticle.objects.filter(is_published=True).order_by('-date')[:2]

    context = {
        'settings': settings,
        'values': values,
        'divisions': divisions,
        'testimonials': testimonials,
        'events': events,
        'featured_event': featured_event,
        'news': news,
    }
    return render(request, 'home.html', context)

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
    video_items = GalleryItem.objects.filter(media_type='VIDEO').order_by('-created_at')
    photo_items = GalleryItem.objects.filter(media_type='PHOTO').order_by('-created_at')
    featured = GalleryItem.objects.filter(is_featured=True).first()

    context = {
        'videos': video_items,
        'photos': photo_items,
        'featured': featured,
    }
    return render(request, 'media.html', context)

def donate(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        amount = request.POST.get('amount')
        custom_amount = request.POST.get('custom_amount')
        donation_type = request.POST.get('donation_type')

        # Use custom amount if provided, otherwise use the selected button amount
        final_amount = custom_amount if custom_amount and custom_amount.strip() else amount

        # Save to database
        DonationSubmission.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            amount=final_amount,
            donation_type=donation_type
        )
        # Redirect or render success page
        return render(request, 'donate_success.html')

    return render(request, 'donate.html')