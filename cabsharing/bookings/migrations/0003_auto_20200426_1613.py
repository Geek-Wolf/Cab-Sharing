# Generated by Django 3.0.3 on 2020-04-26 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_bookings_max_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='max_members',
            field=models.PositiveIntegerField(default=4, help_text='maximum number of members includes you as well.'),
        ),
    ]
