# Generated by Django 3.1.7 on 2021-07-28 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_type', models.CharField(choices=[('Computer', 'Computer'), ('PS3', 'PS3'), ('PS4', 'PS4'), ('PS5', 'PS5'), ('X-BOX', 'X-BOX')], default='Computer', max_length=9)),
                ('device_name', models.CharField(max_length=10)),
                ('price', models.CharField(choices=[('CP_1h', 10000), ('PS3_1h', 30000), ('PS4_1h', 40000), ('PS5_1h', 50000), ('X-BOX_1h', 50000)], default='CP_1h', max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Gamer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RentedDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('finish_time', models.DateTimeField()),
                ('device_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.device')),
                ('gamer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.gamer')),
            ],
        ),
    ]
