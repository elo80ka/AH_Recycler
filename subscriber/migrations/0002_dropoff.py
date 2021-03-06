# Generated by Django 2.0.7 on 2018-07-28 19:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('subscriber', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dropoff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_bottles', models.IntegerField(default=0)),
                ('num_bags', models.IntegerField(default=0)),
                ('dropoff_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriber.Subscriber')),
            ],
        ),
    ]
