# Generated by Django 5.1.2 on 2024-12-02 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_category_icon_alter_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
