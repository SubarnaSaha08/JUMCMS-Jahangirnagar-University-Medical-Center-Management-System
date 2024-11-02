# Generated by Django 4.0.3 on 2024-11-02 09:15

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(help_text='Unique email address for the user.', max_length=255, unique=True, verbose_name='Email')),
                ('name', models.CharField(help_text='Full name of the user.', max_length=200)),
                ('role', models.CharField(choices=[('Doctor', 'Doctor'), ('Student', 'Student'), ('Campus_employee', 'Campus_employee'), ('Storekeeper', 'Storekeeper'), ('Lab_technician', 'Lab_technician'), ('Admin', 'Admin')], help_text='Role of the user (e.g., patient, doctor).', max_length=200)),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], help_text='Blood group of the user.', max_length=200)),
                ('date_of_birth', models.DateField(help_text='Date of birth of the user.')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], help_text='Gender of the user.', max_length=200)),
                ('phone_number', models.CharField(help_text="Phone number of the user, in the format '+880XXXXXXXXXX'.", max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must start with '+880' and be followed by 10 digits.", regex='^\\+880\\d{10}$')])),
                ('profile_picture', models.ImageField(default='profile_pictures/default_user.png', help_text="Path to the user's profile picture.", upload_to='profile_pictures/')),
                ('is_active', models.BooleanField(default=True, help_text='Indicates whether the user is active.')),
                ('is_approved', models.BooleanField(default=False, help_text='Indicates whether the user is approved.')),
                ('is_admin', models.BooleanField(default=False, help_text='Indicates whether the user is an admin.')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Timestamp when the user was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Timestamp when the user was last updated.')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Storekeeper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LabTechnician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_appointments', models.IntegerField(default=0, help_text='Number of appointments for the doctor.')),
                ('no_of_patients', models.IntegerField(default=0, help_text='Number of patients consulted with the doctor.')),
                ('no_of_prescriptions', models.IntegerField(default=0, help_text='Number of prescriptions prepared by the doctor.')),
                ('qualifications', models.CharField(default='MBBS', help_text='Qualifications of the doctor.', max_length=200)),
                ('specialty', models.CharField(default='medicine', help_text='Specialty area of the doctor.', max_length=100)),
                ('experience_years', models.IntegerField(default=0, help_text='Years of experience of the doctor.')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
