# Generated by Django 5.1.4 on 2025-01-11 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='prince',
            new_name='price',
        ),
    ]
