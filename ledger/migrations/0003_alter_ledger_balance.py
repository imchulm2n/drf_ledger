# Generated by Django 4.0.3 on 2023-03-09 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0002_alter_ledger_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger',
            name='balance',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]