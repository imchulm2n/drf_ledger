# Generated by Django 4.0.3 on 2023-03-09 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='urlShortener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longurl', models.CharField(max_length=255)),
                ('shorturl', models.CharField(max_length=10)),
            ],
        ),
    ]
