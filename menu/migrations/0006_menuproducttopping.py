# Generated by Django 4.2 on 2023-05-05 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_remove_menuproduct_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuProductTopping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menuproduct')),
                ('topping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menutopping')),
            ],
        ),
    ]
