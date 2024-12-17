from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title=models.charfield(max_length=100)
    content=models.Textfield()
    created_at=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(on_delete=Models.CASCADE, related_name="notes")
    
    
    def __str__(self):
        return self.title
# Create your models here.