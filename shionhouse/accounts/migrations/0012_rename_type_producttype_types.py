# Generated by Django 5.1.6 on 2025-03-09 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_productcategory_product_productcategoryid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producttype',
            old_name='type',
            new_name='types',
        ),
    ]
