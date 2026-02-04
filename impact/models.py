from django.db import models

# Create your models here.
from django_mongodb_backend.fields import ObjectIdAutoField

class Division(models.Model):
    id = ObjectIdAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='divisions/', blank=True, null=True)
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return self.title