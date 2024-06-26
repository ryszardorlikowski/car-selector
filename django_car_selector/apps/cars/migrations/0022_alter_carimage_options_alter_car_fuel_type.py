# Generated by Django 4.0 on 2023-04-19 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0021_feedback'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carimage',
            options={'ordering': ['image']},
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Petrol'), (2, 'Diesel'), (3, 'Electric'), (4, 'Hybrid petrol'), (5, 'Plug in Hybrid Petrol'), (6, 'Mild Hybrid Petrol'), (7, 'Mild Hybrid Diesel')], null=True),
        ),
    ]
