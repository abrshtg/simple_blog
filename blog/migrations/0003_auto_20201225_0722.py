# Generated by Django 3.1.4 on 2020-12-25 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201225_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wildlife',
            name='img',
            field=models.ImageField(default='', upload_to='pics'),
        ),
    ]
