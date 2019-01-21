# Generated by Django 2.1.1 on 2019-01-21 00:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hearthstone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='user',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
