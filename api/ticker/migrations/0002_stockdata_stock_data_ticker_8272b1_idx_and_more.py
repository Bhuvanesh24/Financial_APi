# Generated by Django 5.0.3 on 2024-03-19 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='stockdata',
            index=models.Index(fields=['ticker'], name='stock_data_ticker_8272b1_idx'),
        ),
        migrations.AddIndex(
            model_name='stockdata',
            index=models.Index(fields=['date'], name='stock_data_date_56db21_idx'),
        ),
    ]
