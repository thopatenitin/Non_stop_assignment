# Generated by Django 3.2.12 on 2023-02-13 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0003_rename_post_content_post_post_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_text',
            new_name='content',
        ),
    ]
