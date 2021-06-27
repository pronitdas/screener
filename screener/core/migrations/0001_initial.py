# Generated by Django 3.2.4 on 2021-06-27 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open', models.FloatField()),
                ('high', models.FloatField()),
                ('date', models.DateField()),
                ('low', models.FloatField()),
                ('adj_close', models.FloatField()),
                ('volume', models.FloatField()),
                ('stock', models.FloatField()),
            ],
        ),
    ]