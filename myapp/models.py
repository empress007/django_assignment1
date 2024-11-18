from django.db import models

# Create your models here.
class Card(models.Model):
    image = models.CharField(max_length=10000, default='image', blank=True, null=True)
    name = models.CharField(max_length=250)
    post = models.TextField(blank=True, null=True)
    like = models.CharField( max_length=7)
    
    # socials
    ig_link = models.URLField()
    x_link = models.URLField()
    linkedIn_link = models.URLField()
    fb_link = models.URLField()
    # update
    whatsapp_number = models.CharField(max_length=11,default='whatsapp number')
    phone_number = models.CharField(max_length=15,default='phone number')
    
    def __str__(self):
        return self.name
        # return f"Name - {self.name}"
        