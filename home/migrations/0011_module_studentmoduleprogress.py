# Generated by Django 4.1.12 on 2024-05-04 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_smishingdetection_join_us'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.skill')),
            ],
        ),
        migrations.CreateModel(
            name='StudentModuleProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.module')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.student')),
            ],
            options={
                'unique_together': {('student', 'module')},
            },
        ),
    ]
