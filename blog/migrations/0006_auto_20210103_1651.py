# Generated by Django 3.1.4 on 2021-01-03 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_wildlife_json'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wildlife',
            name='img',
            field=models.ImageField(blank=True, default='', null=True, upload_to='pics'),
        ),
    ]
