from django.db import models


class ContactUs1(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, default='0000000000')
    email = models.EmailField(max_length=255)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
