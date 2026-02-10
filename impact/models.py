from django.db import models

class Division(models.Model):
    # Standard Django ID (works perfectly with SQLite)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='divisions/', blank=True, null=True)
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return self.title