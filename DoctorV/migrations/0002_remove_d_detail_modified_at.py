# Generated by Django 2.0 on 2022-05-22 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DoctorV', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='d_detail',
            name='modified_at',
        ),
    ]
