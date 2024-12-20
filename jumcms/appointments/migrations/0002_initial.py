# Generated by Django 4.0.3 on 2024-11-15 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appointments', '0001_initial'),
        ('medical_tests', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testappointment',
            name='medical_test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test', to='medical_tests.test'),
        ),
        migrations.AddField(
            model_name='testappointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.patient'),
        ),
        migrations.AddField(
            model_name='doctorappointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_appointments', to='users.doctor'),
        ),
        migrations.AddField(
            model_name='doctorappointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.patient'),
        ),
    ]
