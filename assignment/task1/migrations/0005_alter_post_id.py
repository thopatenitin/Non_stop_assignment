# Generated by Django 3.2.12 on 2023-02-14 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0004_rename_post_text_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
