# Generated by Django 4.2 on 2023-05-04 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuproduct',
            name='price',
        ),
        migrations.CreateModel(
            name='MenuProductPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menusize')),
            ],
        ),
    ]
