# Generated by Django 3.2.4 on 2021-06-27 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210627_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='stock',
            field=models.CharField(max_length=200),
        ),
    ]