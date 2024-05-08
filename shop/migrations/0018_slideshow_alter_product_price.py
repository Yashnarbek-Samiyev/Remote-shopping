# Generated by Django 5.0.4 on 2024-05-08 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_category_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlideShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='slideshow')),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
