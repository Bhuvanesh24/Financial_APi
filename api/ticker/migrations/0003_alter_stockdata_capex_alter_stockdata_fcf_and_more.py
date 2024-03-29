# Generated by Django 5.0.3 on 2024-03-19 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0002_stockdata_stock_data_ticker_8272b1_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockdata',
            name='capex',
            field=models.DecimalField(decimal_places=4, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='fcf',
            field=models.DecimalField(decimal_places=4, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='gp',
            field=models.DecimalField(decimal_places=4, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='revenue',
            field=models.DecimalField(decimal_places=4, max_digits=20, null=True),
        ),
    ]
