# Generated by Django 5.1.6 on 2025-03-14 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_menu_url_sub2menu_url_submenu_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submenu',
            name='menuId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submenus', to='accounts.menu'),
        ),
    ]
