# Generated by Django 2.1.3 on 2019-01-05 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0002_auto_20181129_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
