# Generated by Django 4.2.1 on 2023-05-27 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_arttags_alter_article_options_tag_arttags_article_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ArtTags',
            new_name='Scope',
        ),
    ]