from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from django.conf import settings
from django.urls import reverse
from django.template.defaultfilters import slugify
import uuid
from datetime import datetime
from posts.validation import check_slug_unique
# Create your models here.

#add post time // to do 
class Post(models.Model):
    categories = (
        ('cars', 'Cars'),
        ('electronics', 'Electronics'),
        ('cards', 'Cards'),
        ('clothes', 'Clothes'),
        ('others', 'Others')
    )
    status_choice = (
        (2, 'Pending'),
        (1, 'Approved'),
        (0, 'Denied'),
    )
    
    name = models.CharField(max_length=64, blank=False, null=False, 
                            validators=[MinLengthValidator(6)])
    slug = models.SlugField(max_length=256, unique=True, null=False)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=False, 
                                null=False, validators=[MinValueValidator(0.01)])
    category = models.CharField(max_length=16, choices=categories, blank=False,
                                null=False)
    image = models.ImageField(upload_to='images/', blank=True, null=False)
    created = models.DateTimeField(auto_now_add=True)
    #bool integer // 1 - True // 0 - False // 2 - Pending(none bool)
    #think about better way to implement this field // use cases
    status = models.IntegerField(default=2, choices=status_choice)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             blank=False, null=False)
    

    def get_absolute_url(self):
        return reverse("posts:post", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        slug = check_slug_unique(Post, slugify(self.name))
        self.slug = slug
        return super(Post, self).save(*args, **kwargs)
    
    
class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)
    name = models.CharField(max_length=128, blank=False, null=False,
                            validators=[MinLengthValidator(6)])
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=16, decimal_places=2,
                                blank=False, null=False)
    category = models.CharField(max_length=32, blank=False, null=False)
    post_closed = models.DateTimeField(auto_now_add=True, null=False)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, 
                              on_delete=models.SET_NULL, related_name='buyers', 
                              blank=False, null=True)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, 
                               on_delete=models.SET_NULL, related_name='sellers',
                               blank=False, null=True)
    
    
    
#signals 
#create transaction // to do 
#remove object Post, transaction works as history of deal
