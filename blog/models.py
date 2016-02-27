from django.db import models
from django.utils import timezone


class Post(models.Model):
    STATUSES = (
        ('D', 'Draft'),
        ('P', 'Published')    
    )
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUSES, default='P')
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


