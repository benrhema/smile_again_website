from django.db import models

# --- NEW HUB MODELS ---

class HomeSettings(models.Model):
    """Global text and stats for the Home Page Hub"""
    hero_title = models.CharField(max_length=200, default="SMILE AGAIN", help_text="Use <br> for line breaks")
    hero_description = models.TextField(default="Empowering individuals with disabilities...")
    mission_text = models.TextField(blank=True)
    vision_text = models.TextField(blank=True)
    
    # Counter Stats
    lives_impacted = models.CharField(max_length=20, default="10K+")
    programs_count = models.CharField(max_length=20, default="50+")
    countries_count = models.CharField(max_length=20, default="25+")

    class Meta:
        verbose_name = "Home Global Setting"
        verbose_name_plural = "Home Global Settings"

    def __str__(self):
        return "Global Home Content"

class SiteValue(models.Model):
    """The 4-column values section (Compassion, Community, etc.)"""
    icon = models.CharField(max_length=50, help_text="Emoji or Icon Name")
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    """Success Stories / Success Cards"""
    name = models.CharField(max_length=100)
    program_tag = models.CharField(max_length=100, help_text="e.g. Education Access")
    quote = models.TextField()

    def __str__(self):
        return self.name

class Event(models.Model):
    """Upcoming Events section"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False, help_text="Show in the large yellow box?")
    image = models.ImageField(upload_to='events/', null=True, blank=True)

    def __str__(self):
        return self.title

# --- EXISTING MODELS ---

class Division(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_name = models.CharField(max_length=50, help_text="e.g., 'heart', 'home', 'school'")
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    ROLE_CHOICES = [('LEADERSHIP', 'Leadership'), ('CORE', 'Core Staff'), ('VOLUNTEER', 'Volunteer')]
    name = models.CharField(max_length=100)
    role_title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=ROLE_CHOICES, default='CORE')
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    initials = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name} - {self.role_title}"

class Partner(models.Model):
    CATEGORY_CHOICES = [('CORPORATE', 'Corporate Partner'), ('NGO', 'NGO Ally'), ('GOVT', 'Government Agency')]
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='partners/', blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    short_description = models.CharField(max_length=200, blank=True)
    website_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

class GalleryItem(models.Model):
    TYPE_CHOICES = [('PHOTO', 'Photo'), ('VIDEO', 'Video')]
    title = models.CharField(max_length=200)
    media_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    file = models.FileField(upload_to='gallery/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='gallery/thumbs/', blank=True, null=True)
    video_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# --- NEWS SECTION MODEL ---

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=50, default="Community") 
    author = models.CharField(max_length=100, default="SAO Team")
    date = models.DateField()
    summary = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='news/', null=True, blank=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
class DonationSubmission(models.Model):
    DONATION_TYPES = [('ONE-TIME', 'One-Time'), ('MONTHLY', 'Monthly')]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    amount = models.CharField(max_length=50)  # Stores selected or custom amount
    donation_type = models.CharField(max_length=20, choices=DONATION_TYPES, default='ONE-TIME')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - ${self.amount}"