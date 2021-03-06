# Generated by Django 2.0 on 2022-05-22 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PatientV', '0002_auto_20220522_1209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='p_appointment',
            old_name='Payment_History',
            new_name='Payment_Status',
        ),
        migrations.AddField(
            model_name='p_appointment',
            name='Payment_Time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='p_appointment',
            name='Appointment_Status',
            field=models.CharField(default='Pending', max_length=50),
        ),
    ]
