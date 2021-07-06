# Generated by Django 3.2.4 on 2021-06-14 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator_name', models.CharField(max_length=255)),
                ('creator_age', models.IntegerField()),
                ('creator_location', models.CharField(max_length=255)),
                ('creator_youtubechannel', models.CharField(max_length=255)),
                ('creator_date_joined', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
