# Generated by Django 4.2 on 2023-04-28 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_tags_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]
