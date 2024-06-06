from django.db import models
from django.contrib.auth.models import User
from .utils import generate_slug

# Create your models here.


class Receipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    receipe_name=models.CharField(max_length=100)
    slug = models.SlugField(unique= True)
    receipe_description=models.TextField()
    receipe_image=models.ImageField(upload_to="receipes")
    receipe_view_count=models.IntegerField(default=1)
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.receipe_name)
        super(Receipe, self).save(*args, **kwargs)