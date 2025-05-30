# Generated by Django 5.0.4 on 2024-05-02 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surfScrapperApi', '0002_subscriber_isactive'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('textForHtml', models.CharField(max_length=5000)),
                ('totalScore', models.BooleanField(default=False)),
            ],
        ),
    ]
