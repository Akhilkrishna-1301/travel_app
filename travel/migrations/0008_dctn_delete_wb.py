# Generated by Django 4.1.3 on 2022-12-11 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0007_wb'),
    ]

    operations = [
        migrations.CreateModel(
            name='dctn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('imgs', models.ImageField(upload_to='picture')),
                ('Des', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='wb',
        ),
    ]
