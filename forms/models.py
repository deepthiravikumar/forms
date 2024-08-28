from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField("Date of Birth")
    
    def __str__(self):
        return self.name
