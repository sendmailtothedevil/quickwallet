# Generated by Django 4.0.1 on 2022-02-01 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_wallet_purpose'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='purpose',
        ),
    ]
