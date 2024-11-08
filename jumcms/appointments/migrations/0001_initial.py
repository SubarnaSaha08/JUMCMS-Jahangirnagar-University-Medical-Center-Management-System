# Generated by Django 5.1.2 on 2024-11-08 14:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('scheduled', 'Scheduled'), ('completed', 'Completed'), ('canceled', 'Canceled')], default='scheduled', max_length=20)),
                ('is_emergency', models.BooleanField(default=False, help_text='Indicates whether the appointment is emergency.')),
                ('reason', models.CharField(default='', max_length=200)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_appointments', to='users.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.patient')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('scheduled', 'Scheduled'), ('completed', 'Completed'), ('canceled', 'Canceled')], default='scheduled', max_length=20)),
                ('is_emergency', models.BooleanField(default=False, help_text='Indicates whether the appointment is emergency.')),
                ('lab_technician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_technician', to='users.labtechnician')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
