# Generated by Django 3.0.1 on 2020-01-03 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_auto_20200103_1825'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['date_added']},
        ),
        migrations.AlterModelOptions(
            name='reply',
            options={'ordering': ['date_added'], 'verbose_name_plural': 'replies'},
        ),
    ]
