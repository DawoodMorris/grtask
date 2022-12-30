# Generated by Django 4.1.4 on 2022-12-30 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin', models.DateField(verbose_name='check in data')),
                ('checkout', models.DateField(verbose_name='check out date')),
                ('rental_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grapp.rental')),
            ],
        ),
    ]