# Generated by Django 3.2.12 on 2023-02-13 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-published_date', '-creation_date']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='post_content',
        ),
    ]