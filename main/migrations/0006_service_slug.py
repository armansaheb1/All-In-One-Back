# Generated by Django 5.1.1 on 2024-09-11 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_service_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
