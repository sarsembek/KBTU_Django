# Generated by Django 5.0.6 on 2024-05-23 08:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkusage',
            name='link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usage', to='links_app.link'),
        ),
    ]
