# Generated by Django 4.1.3 on 2023-01-19 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0009_delete_dctn'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='price',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]