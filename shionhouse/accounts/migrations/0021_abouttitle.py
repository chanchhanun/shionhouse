# Generated by Django 5.1.6 on 2025-03-17 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_alter_submenu_menuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('subTitle', models.CharField(max_length=200, null=True)),
                ('popularLocationImage', models.ImageField(blank=True, null=True, upload_to='about/')),
            ],
        ),
    ]
