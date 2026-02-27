from django.db import models

class Division(models.Model):
    """The 'Empowering Lives' sections on the home page"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_name = models.CharField(max_length=50, help_text="e.g., 'heart', 'home', 'school'")
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    """For the 'Our Team' page"""
    ROLE_CHOICES = [
        ('LEADERSHIP', 'Leadership'),
        ('CORE', 'Core Staff'),
        ('VOLUNTEER', 'Volunteer'),
    ]
    name = models.CharField(max_length=100)
    role_title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=ROLE_CHOICES, default='CORE')
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    initials = models.CharField(max_length=2, help_text="Used if no image exists (e.g., 'EM')")

    def __str__(self):
        return f"{self.name} - {self.role_title}"

class Partner(models.Model):
    """For the 'Our Partners' page"""
    CATEGORY_CHOICES = [
        ('CORPORATE', 'Corporate Partner'),
        ('NGO', 'NGO Ally'),
        ('GOVT', 'Government Agency'),
    ]
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='partners/', blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    short_description = models.CharField(max_length=200, blank=True)
    website_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

class GalleryItem(models.Model):
    """For the 'Media Gallery' page"""
    TYPE_CHOICES = [
        ('PHOTO', 'Photo'),
        ('VIDEO', 'Video'),
    ]
    title = models.CharField(max_length=200)
    media_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    file = models.FileField(upload_to='gallery/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='gallery/thumbs/', blank=True, null=True)
    video_url = models.URLField(blank=True, help_text="Link to YouTube/Vimeo if not uploading file")
    is_featured = models.BooleanField(default=False, help_text="Show in the large hero box?")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title