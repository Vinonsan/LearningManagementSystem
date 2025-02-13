# Generated by Django 5.0 on 2023-12-27 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('Course_Name', models.CharField(max_length=150)),
                ('Course_Code', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=False, help_text='0-show,1-Hidden')),
                ('description', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
