# Generated by Django 3.2.3 on 2022-02-28 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0015_alter_posts_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/uploads/'),
        ),
    ]
