# Generated by Django 2.0 on 2022-05-25 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PatientV', '0008_auto_20220524_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='p_appointment',
            name='Diagnosis',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
