# Generated by Django 3.2.25 on 2024-06-04 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_friendy_name_category_friendly_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
