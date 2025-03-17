# Generated by Django 5.1.6 on 2025-03-17 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_abouttitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter', models.CharField(max_length=200, null=True)),
                ('facebook', models.CharField(max_length=200, null=True)),
                ('pinterest', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
