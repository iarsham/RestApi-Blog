# Generated by Django 4.0.4 on 2022-06-11 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Comment', '0003_rename_author_reply_comment_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reply_comment',
            options={'ordering': ['-created'], 'verbose_name': 'Reply Comment', 'verbose_name_plural': 'Reply Comments'},
        ),
    ]
