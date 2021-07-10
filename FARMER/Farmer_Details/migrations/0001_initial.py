# Generated by Django 3.2.5 on 2021-07-08 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=20)),
                ('added_on', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Taluka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taluka_name', models.CharField(max_length=20)),
                ('added_on', models.DateTimeField()),
                ('district_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Farmer_Details.district')),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('village_name', models.CharField(max_length=20)),
                ('added_on', models.DateTimeField()),
                ('taluka_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Farmer_Details.taluka')),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('mobile_number', models.BigIntegerField()),
                ('aadhaar_number', models.BigIntegerField()),
                ('address', models.CharField(max_length=30)),
                ('img_path', models.CharField(max_length=50)),
                ('added_on', models.DateTimeField()),
                ('farmer_active', models.BooleanField(default=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Farmer_Details.district')),
                ('taluka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Farmer_Details.taluka')),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Farmer_Details.village')),
            ],
        ),
    ]
