# Generated by Django 3.2.5 on 2021-07-09 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Farmer_Details', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='img_path',
            field=models.ImageField(upload_to='items'),
        ),
    ]