# Generated by Django 3.1.4 on 2021-01-03 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210103_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wildlife',
            name='img',
            field=models.ImageField(blank=True, default='', null=True, upload_to='pics'),
        ),
    ]
