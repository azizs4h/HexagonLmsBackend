# Generated by Django 3.1.3 on 2021-03-07 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0006_auto_20210307_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonnotes',
            name='note_description',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
