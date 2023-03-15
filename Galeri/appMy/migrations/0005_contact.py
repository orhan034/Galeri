# Generated by Django 4.1.5 on 2023-03-15 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0004_photo_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Kullanıcı Adı')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('subject', models.CharField(max_length=50, verbose_name='Mesaj Konusu')),
                ('text', models.TextField(max_length=1000, verbose_name='Mesaj')),
            ],
        ),
    ]
