# Generated by Django 2.2.1 on 2019-06-18 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppOne', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature', models.ImageField(upload_to='user_signature')),
            ],
        ),
    ]