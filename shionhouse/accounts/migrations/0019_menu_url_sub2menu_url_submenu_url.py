# Generated by Django 5.1.6 on 2025-03-10 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_menu_submenu_sub2menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sub2menu',
            name='url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='submenu',
            name='url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
