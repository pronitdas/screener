# Generated by Django 3.2.4 on 2021-06-27 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='stock',
            index=models.Index(fields=['stock'], name='core_stock_stock_2886c0_idx'),
        ),
        migrations.AddIndex(
            model_name='stock',
            index=models.Index(fields=['date'], name='core_stock_date_172dc8_idx'),
        ),
        migrations.AddConstraint(
            model_name='stock',
            constraint=models.UniqueConstraint(fields=('stock', 'date'), name='unique_stock_date'),
        ),
    ]
