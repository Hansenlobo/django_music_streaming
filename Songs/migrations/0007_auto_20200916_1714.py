# Generated by Django 3.1.1 on 2020-09-16 11:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Songs', '0006_auto_20200916_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='konkanisongs',
            name='album_slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='konkanisongs',
            name='album',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]