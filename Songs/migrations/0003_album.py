# Generated by Django 3.1.1 on 2020-09-15 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Songs', '0002_auto_20200915_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('albumName', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, default='album.png', null=True, upload_to='albumpic')),
                ('artistName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Songs.singer')),
            ],
        ),
    ]
