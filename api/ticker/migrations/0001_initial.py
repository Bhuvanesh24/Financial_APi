

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ticker', models.CharField(max_length=10)),
                ('date', models.DateField(null=True)),
                ('revenue', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('gp', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('fcf', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('capex', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'stock_data',
            },
        ),
    ]
