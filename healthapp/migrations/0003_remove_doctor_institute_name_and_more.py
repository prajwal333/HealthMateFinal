# Generated by Django 4.0.3 on 2023-05-29 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0002_remove_doctor_location_doctor_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='institute_name',
        ),
        migrations.AddField(
            model_name='doctor',
            name='education_training',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='doctor',
            name='professional_experience',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('Dentistry', 'Dentistry'), ('Cardiology', 'Cardiology'), ('ENT Specialists', 'ENT Specialists'), ('Dietitian', 'Dietitian'), ('Endocrinology', 'Endocrinology'), ('Blood Screening', 'Blood Screening'), ('Eye Care', 'Eye Care'), ('Physical Therapy', 'Physical Therapy'), ('Neurology', 'Neurology'), ('Gynaecology', 'Gynaecology'), ('Pediatrics', 'Pediatrics'), ('Ophthalmology', 'Ophthalmology'), ('Orthopedic', 'Orthopedic'), ('Pulmonologist', 'Pulmonologist'), ('Radiologist', 'Radiologist'), ('General Surgeon', 'General Surgeon')], max_length=100),
        ),
    ]