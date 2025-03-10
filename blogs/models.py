from django.db import models
from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from PIL import Image
from io import BytesIO
import os
from django.core.files import File
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Yazan')
    image = models.ImageField(verbose_name='Resim',blank=True,null=True)
    caption = models.CharField(max_length=100, verbose_name='Başlık')
    description = models.CharField(max_length=100, blank=True,null=True,verbose_name='Açıklama')
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    content = RichTextUploadingField()  # CKEditor alanı
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def get_absolute_url(self):
        return reverse("blog-detail", args=[str(self.slug)])
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.caption

    def save(self, *args, **kwargs):

        try:
            # Check if the category already exists
            existing_instance = Blog.objects.get(id=self.id)
            if self.image and existing_instance.image != self.image:
                img = Image.open(self.image)
                
                # Convert RGBA images to RGB
                if img.mode in ('RGBA', 'LA'):
                    background = Image.new('RGB', img.size, 'white')
                    background.paste(img, mask=img.split()[-1])
                    img = background

                # Resize image
                max_size = (1000, 1000)
                img.thumbnail(max_size, Image.Resampling.LANCZOS)

                # Save as WebP
                buffer = BytesIO()
                img.save(buffer, format='WebP', quality=85, optimize=True)
                
                # Create a new file name
                name = os.path.splitext(self.image.name)[0]
                new_name = f"{name}.webp"
                
                # Assign the processed file back to the image field
                self.image = File(buffer, name=new_name)
        except Blog.DoesNotExist:
            # Handle new instances
            if self.image:
                img = Image.open(self.image)
                
                # Convert RGBA images to RGB
                if img.mode in ('RGBA', 'LA'):
                    background = Image.new('RGB', img.size, 'white')
                    background.paste(img, mask=img.split()[-1])
                    img = background

                # Resize image
                max_size = (1000, 1000)
                img.thumbnail(max_size, Image.Resampling.LANCZOS)

                # Save as WebP
                buffer = BytesIO()
                img.save(buffer, format='WebP', quality=85, optimize=True)
                
                # Create a new file name
                name = os.path.splitext(self.image.name)[0]
                new_name = f"{name}.webp"
                
                # Assign the processed file back to the image field
                self.image = File(buffer, name=new_name)

        # Save the instance after processing
        super().save(*args, **kwargs)
    