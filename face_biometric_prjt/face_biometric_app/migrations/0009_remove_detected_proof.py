# Generated by Django 4.0.3 on 2022-06-24 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('face_biometric_app', '0008_detected_proof'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detected',
            name='proof',
        ),
    ]
