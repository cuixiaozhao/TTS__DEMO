# Generated by Django 2.1.3 on 2018-11-29 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskorder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskordermanage',
            name='order_number',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='单号'),
        ),
    ]
