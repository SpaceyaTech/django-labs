# Generated by Django 5.0.4 on 2024-04-12 19:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stori', '0003_blog_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='Category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='stori.category'),
            preserve_default=False,
        ),
    ]
