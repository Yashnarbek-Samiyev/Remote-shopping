# Generated by Django 5.0.4 on 2024-05-04 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_category_is_sub_category_sub_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='sub_category',
        ),
    ]
