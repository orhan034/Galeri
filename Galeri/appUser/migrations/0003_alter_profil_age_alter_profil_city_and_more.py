# Generated by Django 4.1.5 on 2023-03-14 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0002_alter_profil_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='age',
            field=models.IntegerField(default='-', verbose_name='Yaş'),
        ),
        migrations.AlterField(
            model_name='profil',
            name='city',
            field=models.CharField(default='-', max_length=50, verbose_name='Yaşadığınız Yer'),
        ),
        migrations.AlterField(
            model_name='profil',
            name='degree',
            field=models.CharField(default='-', max_length=50, verbose_name='Tahsil'),
        ),
        migrations.AlterField(
            model_name='profil',
            name='email',
            field=models.CharField(default='-', max_length=50, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='profil',
            name='job',
            field=models.CharField(default='-', max_length=50, verbose_name='İş'),
        ),
        migrations.AlterField(
            model_name='profil',
            name='phone',
            field=models.CharField(default='-', max_length=50, verbose_name='Telefon Numarası'),
        ),
        migrations.AlterField(
            model_name='profil',
            name='text',
            field=models.TextField(default='-', max_length=1000, verbose_name='Hakkımda'),
        ),
        migrations.AlterField(
            model_name='profil',
            name='website',
            field=models.URLField(default='-', verbose_name='Website'),
        ),
    ]
