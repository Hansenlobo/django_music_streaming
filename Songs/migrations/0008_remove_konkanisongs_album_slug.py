# Generated by Django 3.1.1 on 2020-09-16 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Songs', '0007_auto_20200916_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='konkanisongs',
            name='album_slug',
        ),
    ]
