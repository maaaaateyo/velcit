# Generated by Django 5.0.1 on 2024-01-22 11:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.room'),
        ),
    ]
