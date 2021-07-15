# Generated by Django 3.2.5 on 2021-07-14 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Brand', '0006_alter_brandadcard_brand_campaign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandadcard',
            name='brand_organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='b_org_id', to='Brand.brandorganization'),
        ),
    ]
