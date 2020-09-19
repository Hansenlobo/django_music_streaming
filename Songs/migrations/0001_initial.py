# Generated by Django 3.1.1 on 2020-09-15 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artistName', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='')),
                ('description', models.TextField()),
            ],
        ),
    ]
