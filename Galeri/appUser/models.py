from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profil(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    birthday = models.DateField(("Doğum Yılı"), auto_now_add=False, null= True)
    age = models.IntegerField(("Yaş"), default=0)
    website = models.URLField(("Website"), max_length=200, default='-')
    degree = models.CharField(("Tahsil"), max_length=50, default='-')
    phone = models.CharField(("Telefon Numarası"), max_length=50, default='-')
    email = models.CharField(("Email"), max_length=50, default='-')
    city = models.CharField(("Yaşadığınız Yer"), max_length=50, default='-')
    job = models.CharField(("İş"), max_length=50, default='-')
    text = models.TextField(("Hakkımda"), max_length=1000, default='-')
    image = models.ImageField(("Profil Resmi"), upload_to='', default='img7.jfif')

    def __str__(self):
        return self.user.username