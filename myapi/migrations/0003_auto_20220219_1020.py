# Generated by Django 3.2.3 on 2022-02-19 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_auto_20220218_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('phone', models.CharField(max_length=30)),
                ('pass1', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-date']},
        ),
    ]
