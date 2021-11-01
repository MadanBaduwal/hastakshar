# Generated by Django 2.2.1 on 2019-07-02 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppOne', '0003_custom_user_signature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custom_user',
            name='signature',
        ),
        migrations.AddField(
            model_name='signature',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]