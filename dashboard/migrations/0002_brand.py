# Generated by Django 3.2.4 on 2021-06-15 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_company_name', models.CharField(max_length=255)),
                ('brand_ad_campaign_in_progress', models.BooleanField(default=False)),
                ('brand_ad_cards_available', models.IntegerField(default=0)),
                ('brand_ad_cards_in_progress', models.IntegerField(default=0)),
                ('brand_ad_cards_complete', models.IntegerField(default=0)),
            ],
        ),
    ]
