# Generated by Django 2.1.1 on 2018-10-12 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('africastalking', '0002_ussdsession'),
    ]

    operations = [
        migrations.AddField(
            model_name='ussdsession',
            name='last_response',
            field=models.TextField(blank=True, null=True),
        ),
    ]
