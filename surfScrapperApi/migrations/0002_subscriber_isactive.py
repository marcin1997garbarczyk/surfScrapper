# Generated by Django 5.0.4 on 2024-04-26 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surfScrapperApi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
    ]
