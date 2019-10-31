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

    # This is Django convention, recommended for use
    def get_absolute_url(self):
        return f"{self.slug}"

    # This is NOT Django convention, custom uses, not necessary
    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    # This is NOT Django convention, custom uses, not necessary
    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"
