# Generated by Django 4.1.5 on 2023-01-15 15:36

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_alter_propertytype_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bill',
            options={'ordering': ['-bill_date'], 'verbose_name_plural': 'bills'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['user'], 'verbose_name_plural': 'customers'},
        ),
        migrations.AlterModelOptions(
            name='energyvoucher',
            options={'ordering': ['code'], 'verbose_name_plural': 'energy vouchers'},
        ),
        migrations.AlterModelOptions(
            name='meterreading',
            options={'ordering': ['-submission_date'], 'verbose_name_plural': 'meter readings'},
        ),
        migrations.AlterModelOptions(
            name='propertytype',
            options={'ordering': ['name'], 'verbose_name_plural': 'property types'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='voucher_code',
            field=models.CharField(blank=True, max_length=8, null=True, unique=True),
        ),
        migrations.AlterModelTable(
            name='bill',
            table='bill',
        ),
        migrations.AlterModelTable(
            name='customer',
            table='customer',
        ),
        migrations.AlterModelTable(
            name='energyvoucher',
            table='energy_voucher',
        ),
        migrations.AlterModelTable(
            name='meterreading',
            table='meter_reading',
        ),
        migrations.AlterModelTable(
            name='propertytype',
            table='property_type',
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(default=datetime.date.today)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'payments',
                'db_table': 'payment',
                'ordering': ['-payment_date'],
            },
        ),
    ]
