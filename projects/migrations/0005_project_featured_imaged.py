# Generated by Django 4.1.4 on 2023-02-19 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_tag_project_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_imaged',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]