# Generated by Django 2.1.1 on 2018-10-28 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20181028_1912'),
        ('africastalking', '0006_auto_20181028_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outgoingmessages',
            name='cost',
        ),
        migrations.AddField(
            model_name='outgoingmessages',
            name='charge',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.AccountCharges'),
        ),
    ]
