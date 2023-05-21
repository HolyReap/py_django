from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    image = models.CharField(max_length=200)
    release_date = models.DateField() 
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

