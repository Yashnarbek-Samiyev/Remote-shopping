# Generated by Django 5.0.4 on 2024-05-05 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_remove_category_sub_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]
