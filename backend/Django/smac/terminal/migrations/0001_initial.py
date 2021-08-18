# Generated by Django 3.2.6 on 2021-08-17 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContainerState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('container_number', models.CharField(max_length=255)),
                ('resource_weight', models.IntegerField(default=0)),
                ('state', models.CharField(max_length=4)),
                ('yard_location', models.CharField(max_length=3)),
                ('booking_note', models.CharField(max_length=255)),
                ('stack_location', models.CharField(max_length=255)),
                ('start_time', models.DateTimeField()),
                ('first_time', models.DateTimeField()),
                ('second_time', models.DateTimeField()),
                ('third_time', models.DateTimeField()),
                ('complete_time', models.DateTimeField()),
            ],
        ),
    ]