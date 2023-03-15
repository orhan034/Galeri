from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(("Kategori"), max_length=50)
    slug = models.SlugField(("Slug Kategori"), null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Photo(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE, null=True)
    title = models.CharField(("Fotograf"), max_length=50)
    tetx = models.TextField(("Resim Hakkında"), max_length=1000)
    image = models.ImageField(("Resim"), upload_to='photo')
    date_time = models.DateTimeField(("Tarih"), auto_now_add=True, null=True)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(("Kullanıcı Adı"), max_length=50)
    email = models.CharField(("Email"), max_length=50)
    subject = models.CharField(("Mesaj Konusu"), max_length=50)
    text = models.TextField(("Mesaj"), max_length=1000)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name=("Yorumu Yapan"), on_delete=models.CASCADE)    
    photo = models.ForeignKey(Photo, verbose_name=("Resim"), on_delete=models.CASCADE, null=True)
    title = models.CharField(("Yorum Başlığı"), max_length=50)
    text = models.CharField(("Yorum"), max_length=50)
    date_now = models.DateTimeField(("Zaman"), auto_now_add=True) 
    def __str__(self) :
        return self.title
