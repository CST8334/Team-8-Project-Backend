# Generated by Django 3.2.4 on 2021-06-16 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20210615_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creatoradcard',
            name='ad_card_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.adcard'),
        ),
        migrations.AlterField(
            model_name='creatoradcard',
            name='creator_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.creator'),
        ),
    ]
