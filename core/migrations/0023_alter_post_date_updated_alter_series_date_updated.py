# Generated by Django 4.0.2 on 2022-03-04 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_post_canonical_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
