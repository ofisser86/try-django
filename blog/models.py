from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


User = settings.AUTH_USER_MODEL


class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()


# Create your models here.
class BlogPost(models.Model):  # blogpost_set --> queryset posts for current user object
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    image = models.FileField(upload_to='image', null=True, blank=True)
    title = models.CharField(max_length=256)
    content = models.TextField(null=True, blank=True)
    # For slug in url instead id for readable reasons
    slug = models.SlugField(unique=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = BlogPostManager()

    class Meta:
        ordering = ['-pk', '-publish_date', '-updated', '-timestamp']

    # This is Django convention, recommended for use
    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.slug)])

    # This is NOT Django convention, custom uses, not necessary
    def get_edit_url(self):
        return reverse('update-post', args=[str(self.slug)])

    # This is NOT Django convention, custom uses, not necessary
    def get_delete_url(self):
        return reverse('delete-post', args=[str(self.slug)])
