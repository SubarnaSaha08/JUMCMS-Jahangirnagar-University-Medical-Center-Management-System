# Generated by Django 4.0.3 on 2024-11-13 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundraisingRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_name', models.CharField(max_length=255)),
                ('amount_needed', models.DecimalField(decimal_places=2, max_digits=10)),
                ('details', models.TextField(blank=True, null=True)),
                ('attachments', models.FileField(blank=True, null=True, upload_to='fundraising/')),
                ('is_approved', models.BooleanField(default=False)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.patient')),
            ],
        ),
        migrations.CreateModel(
            name='FundraisingCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_issued_date', models.DateField(auto_now_add=True)),
                ('attachments', models.FileField(blank=True, null=True, upload_to='fundraising_certificates/')),
                ('fundraising_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certifications.fundraisingrequest')),
            ],
        ),
    ]
