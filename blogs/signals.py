from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Blog

@receiver(pre_save, sender=Blog)
def create_blog_slug(sender, instance, **kwargs):
    if not instance.slug:
        base_slug = slugify(instance.caption)
        unique_slug = base_slug
        counter = 1
        # Benzersiz slug oluşturana kadar döngü
        while Blog.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{base_slug}-{counter}"
            counter += 1
        instance.slug = unique_slug 