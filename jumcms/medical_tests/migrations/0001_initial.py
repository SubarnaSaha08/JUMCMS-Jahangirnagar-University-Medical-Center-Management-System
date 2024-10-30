# Generated by Django 4.0.3 on 2024-10-30 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicines', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrescribedTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True, null=True)),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescribed_tests', to='medicines.prescription')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('department', models.CharField(blank=True, max_length=255, null=True)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_date', models.DateField(auto_now_add=True)),
                ('result', models.TextField()),
                ('attached_file', models.FileField(blank=True, null=True, upload_to='test_reports/')),
                ('notes', models.TextField(blank=True, null=True)),
                ('prescribed_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_reports', to='medical_tests.prescribedtest')),
            ],
        ),
        migrations.AddField(
            model_name='prescribedtest',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical_tests.test'),
        ),
    ]
