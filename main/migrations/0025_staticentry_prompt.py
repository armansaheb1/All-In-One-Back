# Generated by Django 5.1.2 on 2024-10-29 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_staticentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticentry',
            name='prompt',
            field=models.TextField(null=True),
        ),
    ]
