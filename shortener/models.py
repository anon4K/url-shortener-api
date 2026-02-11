from django.db import models
import string
import random

def generate_short_code():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=6))

class URL(models.Model):
    original_url = models.URLField(max_length=2000)
    short_code = models.CharField(max_length=10, unique=True, default=generate_short_code)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return f"{self.short_code} -> {self.original_url[:50]}"
    
    @property
    def short_url(self):
        return f"http://localhost:8000/{self.short_code}"
# Create your models here.
