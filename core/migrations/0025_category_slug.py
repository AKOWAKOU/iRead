# Generated by Django 4.0.2 on 2022-03-13 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_remove_category_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=127, null=True, unique=True),
        ),
    ]
