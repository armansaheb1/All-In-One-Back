# Generated by Django 5.1.2 on 2024-10-29 18:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_alter_service_variables'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='template',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)], verbose_name=[(1, 'First'), (2, 'Second'), (3, 'Third')]),
        ),
    ]
