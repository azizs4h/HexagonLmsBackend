# Generated by Django 3.1.3 on 2021-06-14 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0002_auto_20210614_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='meet',
            name='meet_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
