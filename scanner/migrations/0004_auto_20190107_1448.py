# Generated by Django 2.1.3 on 2019-01-07 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0003_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]
