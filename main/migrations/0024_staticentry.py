# Generated by Django 5.1.2 on 2024-10-29 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_remove_newsservice_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90, null=True)),
                ('options', models.JSONField()),
            ],
        ),
    ]
