# Generated by Django 2.1.2 on 2018-11-13 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0005_auto_20181023_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='EndOfDayDataTable',
            fields=[
                ('primary_key', models.AutoField(primary_key=True, serialize=False)),
                ('symbol', models.CharField(blank=True, max_length=7, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('open', models.FloatField(blank=True, null=True)),
                ('high', models.FloatField(blank=True, null=True)),
                ('low', models.FloatField(blank=True, null=True)),
                ('close', models.FloatField(blank=True, null=True)),
                ('volume', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'end_of_day_data_table',
            },
        ),
    ]
