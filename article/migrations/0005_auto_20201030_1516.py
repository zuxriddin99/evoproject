# Generated by Django 3.1.2 on 2020-10-30 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20201030_0307'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlecomment',
            options={'verbose_name': 'ArticleComment', 'verbose_name_plural': 'ArticleComments'},
        ),
    ]
