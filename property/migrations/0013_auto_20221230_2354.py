# Generated by Django 2.2.24 on 2022-12-30 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20221230_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(related_name='owners', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]