# Generated by Django 2.1.1 on 2018-10-20 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('africastalking', '0003_ussdsession_last_response'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ussdsession',
            options={'ordering': ['modified'], 'verbose_name': 'Ussd Session', 'verbose_name_plural': 'Ussd Sessions'},
        ),
        migrations.AlterField(
            model_name='ussdsession',
            name='session_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
