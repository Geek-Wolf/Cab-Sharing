# Generated by Django 3.0.3 on 2020-04-29 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0009_auto_20200429_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='gender',
            field=models.CharField(choices=[('both', 'all'), ('girls', 'only girls'), ('boys', 'only boys')], default='both', max_length=20),
        ),
    ]
