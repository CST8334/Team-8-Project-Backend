# Generated by Django 3.2.5 on 2021-07-13 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Brand', '0003_auto_20210713_1346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brandadcard',
            old_name='brand_campaign_id',
            new_name='brand_campaign',
        ),
        migrations.RenameField(
            model_name='brandadcard',
            old_name='brand_organization_id',
            new_name='brand_organization',
        ),
        migrations.RenameField(
            model_name='brandadcard',
            old_name='brand_user_id',
            new_name='brand_user',
        ),
        migrations.RenameField(
            model_name='brandadcard',
            old_name='creator_campaign_id',
            new_name='creator_campaign',
        ),
        migrations.RenameField(
            model_name='brandadcard',
            old_name='creator_user_id',
            new_name='creator_user',
        ),
    ]
