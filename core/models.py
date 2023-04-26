from django.db import models
from django.utils import timezone
from django.urls import reverse


class Work(models.Model):

    title = models.CharField(max_length=300)
    slug = models.CharField(max_length=250, default='')
    category = models.CharField(max_length=300, default='')
    link = models.URLField(max_length=500, default='')
    cover = models.ImageField(upload_to='works/', default='')
    content = models.TextField(default='')
    published = models.DateTimeField(default=timezone.now)
    changed = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('core:work', args=[self.pk])

    def __str__(self):
        return self.title