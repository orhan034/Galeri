# Generated by Django 4.1.5 on 2023-03-15 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='photo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.photo', verbose_name='Resim'),
        ),
    ]
