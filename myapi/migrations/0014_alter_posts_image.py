# Generated by Django 3.2.3 on 2022-02-28 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0013_auto_20220228_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, default='no', null=True, upload_to='uploads/'),
        ),
    ]
