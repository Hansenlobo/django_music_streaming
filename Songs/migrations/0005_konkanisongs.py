# Generated by Django 3.1.1 on 2020-09-15 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Songs', '0004_auto_20200915_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='KonkaniSongs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
                ('music_file', models.FileField(upload_to='KonkaniSongs/')),
                ('description', models.TextField()),
            ],
        ),
    ]