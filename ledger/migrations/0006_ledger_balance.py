# Generated by Django 4.0.3 on 2023-03-09 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0005_remove_ledger_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='ledger',
            name='balance',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
