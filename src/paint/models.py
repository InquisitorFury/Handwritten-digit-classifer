from django.db import models

# Create your models here.
class Digit(models.Model):
    image = models.ImageField(upload_to='images')
    result = models.CharField(max_length=2, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    
   # def save(self, *args, **kwargs):
    #    return super().save(*args, **kwargs)