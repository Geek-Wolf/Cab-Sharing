# Generated by Django 3.0.3 on 2020-04-28 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20200428_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('message', models.CharField(max_length=500)),
                ('photo', models.ImageField(upload_to='')),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_members', to='bookings.Booking')),
            ],
        ),
    ]