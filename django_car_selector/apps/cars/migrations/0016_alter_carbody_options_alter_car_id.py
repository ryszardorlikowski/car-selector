# Generated by Django 4.0 on 2022-12-31 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0015_remove_car_car_for_man_remove_car_car_for_woman_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carbody',
            options={'ordering': ('order', 'name'), 'verbose_name_plural': 'Car bodies'},
        ),
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
