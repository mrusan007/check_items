# Generated by Django 3.2.8 on 2021-10-12 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_address',
            field=models.CharField(default='sv.Klara 190', max_length=256),
            preserve_default=False,
        ),
    ]
