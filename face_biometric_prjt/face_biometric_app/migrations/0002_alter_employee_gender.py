# Generated by Django 4.0.3 on 2022-06-06 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face_biometric_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=50, null=True),
        ),
    ]