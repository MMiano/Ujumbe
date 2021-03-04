# Generated by Django 2.1.1 on 2018-10-20 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0004_auto_20181020_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentweather',
            name='handler',
            field=models.CharField(choices=[('NETATMO', 'netatmo'), ('OPENWEATHER', 'openweather')], default='OPENWEATHER', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='forecastweather',
            name='handler',
            field=models.CharField(choices=[('NETATMO', 'netatmo'), ('OPENWEATHER', 'openweather')], default='OPENWEATHER', max_length=30),
            preserve_default=False,
        ),
    ]
