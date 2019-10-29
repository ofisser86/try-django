from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL


# Create your models here.
class BlogPost(models.Model):  # blogpost_set --> queryset posts for current user object
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=256)
    content = models.TextField(null=True, blank=True)
    # For slug in url instead id for readable reasons
    slug = models.SlugField(unique=True)
