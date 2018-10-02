# Generated by Django 2.1 on 2018-10-02 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation_Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rev_id', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('message', models.CharField(max_length=1000)),
                ('ad_owner', models.CharField(max_length=100)),
                ('ad_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_id', models.IntegerField()),
                ('list_of_reviews', models.CharField(blank=True, max_length=1000, null=True)),
                ('list_of_events', models.CharField(blank=True, max_length=1000, null=True)),
                ('poster', models.CharField(blank=True, max_length=1000, null=True)),
                ('accommodation_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('accommodation_description', models.CharField(blank=True, max_length=1000, null=True)),
                ('house_rules', models.CharField(blank=True, max_length=1000, null=True)),
                ('booking_rules', models.CharField(blank=True, max_length=1000, null=True)),
                ('amenities', models.CharField(blank=True, max_length=1000, null=True)),
                ('base_price', models.FloatField(blank=True, max_length=1000, null=True)),
                ('num_guests', models.IntegerField(blank=True, null=True)),
                ('num_bedrooms', models.IntegerField(blank=True, null=True)),
                ('num_bathrooms', models.IntegerField(blank=True, null=True)),
                ('suburb', models.CharField(blank=True, max_length=1000, null=True)),
                ('state', models.CharField(blank=True, max_length=1000, null=True)),
                ('country', models.CharField(blank=True, max_length=1000, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.IntegerField()),
                ('ad_owner', models.CharField(max_length=100)),
                ('ad_id', models.IntegerField()),
                ('start_day', models.DateField(help_text='Start day of the rent', verbose_name='Start day of the rent')),
                ('start_day_start_time', models.TimeField(help_text='Starting time', verbose_name='Starting time')),
                ('end_day', models.DateField(help_text='End day of the event', verbose_name='End day of the event')),
                ('end_day_end_time', models.TimeField(help_text='End time', verbose_name='End time')),
                ('notes', models.TextField(blank=True, help_text='Notes', null=True, verbose_name='Notes')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_id', models.IntegerField()),
                ('ad_owner', models.CharField(max_length=100)),
                ('ad_id', models.IntegerField()),
                ('pic', models.CharField(max_length=500000)),
            ],
        ),
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('profile_pic', models.CharField(blank=True, max_length=1000, null=True)),
                ('list_of_ads', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
