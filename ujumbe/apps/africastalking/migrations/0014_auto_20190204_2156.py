# Generated by Django 2.1.1 on 2019-02-04 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('africastalking', '0013_incomingmessage_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomingmessage',
            name='response',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]