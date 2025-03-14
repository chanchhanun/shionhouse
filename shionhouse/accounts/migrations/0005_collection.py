# Generated by Django 5.1.6 on 2025-03-06 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_popularproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collectionImage', models.ImageField(blank=True, null=True, upload_to='collection_image/')),
                ('collectionCaption', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
