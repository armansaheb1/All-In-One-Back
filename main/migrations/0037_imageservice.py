# Generated by Django 5.1.2 on 2024-11-02 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_alter_file_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('prompt', models.TextField(null=True)),
            ],
        ),
    ]