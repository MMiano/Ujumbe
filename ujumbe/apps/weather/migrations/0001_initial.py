# Generated by Django 2.1.1 on 2018-10-06 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('alpha2', models.CharField(max_length=2, unique=True)),
                ('alpha3', models.CharField(max_length=3, unique=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='country_create', to=settings.AUTH_USER_MODEL, verbose_name='author')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='country_update', to=settings.AUTH_USER_MODEL, verbose_name='last updated by')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CurrentWeather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('summary', models.CharField(default='', max_length=255)),
                ('temperature', models.IntegerField(default=0)),
                ('pressure', models.IntegerField(default=0)),
                ('humidity', models.IntegerField(default=0)),
                ('temp_min', models.IntegerField(default=0)),
                ('temp_max', models.IntegerField(default=0)),
                ('visibility', models.IntegerField(default=0)),
                ('wind_speed', models.IntegerField(default=0)),
                ('wind_degree', models.IntegerField(default=0)),
                ('clouds_all', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Current Weather',
                'verbose_name_plural': 'Current Weather',
            },
        ),
        migrations.CreateModel(
            name='ForecastWeather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('summary', models.CharField(default='', max_length=255)),
                ('temperature', models.IntegerField(default=0)),
                ('pressure', models.IntegerField(default=0)),
                ('humidity', models.IntegerField(default=0)),
                ('temp_min', models.IntegerField(default=0)),
                ('temp_max', models.IntegerField(default=0)),
                ('visibility', models.IntegerField(default=0)),
                ('wind_speed', models.IntegerField(default=0)),
                ('wind_degree', models.IntegerField(default=0)),
                ('clouds_all', models.IntegerField(default=0)),
                ('period', models.DurationField()),
            ],
            options={
                'verbose_name': 'Forecast Weather',
                'verbose_name_plural': 'Forecast Weather',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('latitude', models.FloatField(default=0)),
                ('longitude', models.FloatField(default=0)),
                ('name', models.CharField(max_length=255)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='location_create', to=settings.AUTH_USER_MODEL, verbose_name='author')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='weather.Country')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='location_update', to=settings.AUTH_USER_MODEL, verbose_name='last updated by')),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='forecastweather',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='weather.Location'),
        ),
        migrations.AddField(
            model_name='currentweather',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='weather.Location'),
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together={('latitude', 'longitude')},
        ),
    ]