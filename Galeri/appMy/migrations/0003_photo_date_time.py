# Generated by Django 4.1.5 on 2023-03-14 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0002_photo_category_alter_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Tarih'),
        ),
    ]
