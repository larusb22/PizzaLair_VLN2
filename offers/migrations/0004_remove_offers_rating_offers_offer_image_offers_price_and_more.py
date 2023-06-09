# Generated by Django 4.2 on 2023-05-12 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0003_remove_offers_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offers',
            name='rating',
        ),
        migrations.AddField(
            model_name='offers',
            name='offer_image',
            field=models.CharField(default='', max_length=9999),
        ),
        migrations.AddField(
            model_name='offers',
            name='price',
            field=models.DecimalField(decimal_places=0, default=1490, max_digits=8),
        ),
        migrations.DeleteModel(
            name='OfferRating',
        ),
    ]
