# Generated by Django 2.0 on 2022-06-02 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PatientV', '0019_auto_20220531_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='p_detail',
            name='Patient_Status',
            field=models.CharField(default='Patient Exists', max_length=30),
        ),
    ]
