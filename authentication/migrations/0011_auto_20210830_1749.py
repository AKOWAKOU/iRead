# Generated by Django 3.2.4 on 2021-08-30 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_followersmodel_follower'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sociallinks',
            name='twitter_url',
        ),
        migrations.AddField(
            model_name='sociallinks',
            name='twitter_username',
            field=models.CharField(blank=True, max_length=63, verbose_name='twitter link'),
        ),
    ]