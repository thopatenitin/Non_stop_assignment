# Generated by Django 3.2.12 on 2023-02-13 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0002_auto_20230213_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_content',
            new_name='post_text',
        ),
    ]