# Generated by Django 5.2 on 2025-04-10 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('technologies', models.CharField(max_length=500)),
                ('github_link', models.URLField(blank=True, null=True)),
                ('live_link', models.URLField(blank=True, null=True)),
                ('tags', models.CharField(blank=True, max_length=300)),
                ('image', models.ImageField(blank=True, upload_to='project_images/')),
            ],
        ),
    ]
