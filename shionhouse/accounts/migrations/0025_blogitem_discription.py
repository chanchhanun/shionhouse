# Generated by Django 5.1.6 on 2025-03-20 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_mediabodycontact'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogitem',
            name='discription',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
