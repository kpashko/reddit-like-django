from django.db import models

from django.db.models.signals import pre_save, post_delete
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import User


class BlogPost(models.Model):
    title                   = models.CharField(max_length=50, null=False, blank=False)
    body                    = models.CharField(max_length=8000, null=False, blank=False)
    date_published          = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated            = models.DateTimeField(auto_now=True, verbose_name="date updated")
    author                  = models.ForeignKey(User, on_delete=models.CASCADE)
    slug                    = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post                    = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author                  = models.CharField(max_length=200)
    text                    = models.TextField()
    created_date            = models.DateTimeField(auto_now=True, verbose_name="time created")
    approved_comment        = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


def pre_save_blog_post_receiver(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + "-" + instance.title)


pre_save.connect(pre_save_blog_post_receiver, sender=BlogPost)
