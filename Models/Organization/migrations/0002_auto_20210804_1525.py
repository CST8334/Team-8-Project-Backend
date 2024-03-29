# Generated by Django 3.2.5 on 2021-08-04 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Brand', '0002_auto_20210804_1525'),
        ('Organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationmembership',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='org_id_fk', to='Brand.brandorganization'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organizationmembership',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_id_fk', to='Users.customuser'),
            preserve_default=False,
        ),
    ]
