from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from django.conf import settings
from django.urls import reverse
from django.template.defaultfilters import slugify
import uuid

# Create your models here.



class Post(models.Model):
    
    categories = (
        ('cars', 'Cars'),
        ('electronics', 'Electronics'),
        ('cards', 'Cards'),
        ('clothes', 'Clothes'),
        ('others', 'Others')
    )
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, 
                            editable=False)
    slug = models.SlugField(max_length=256, null=False)
    name = models.CharField(max_length=64, blank=False, null=False, 
                            validators=[MinLengthValidator(6)])
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=False, 
                                null=False, validators=[MinValueValidator(0.01)])
    category = models.CharField(max_length=16, choices=categories, blank=False,
                                null=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             blank=False, null=False)
    

    def get_absolute_url(self):
        return reverse("posts:post", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        
        return super(Post, self).save(*args, **kwargs)