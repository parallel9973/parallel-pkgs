# Generated by Django 2.2.1 on 2019-06-15 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.TextField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='about')),
            ],
            options={
                'verbose_name': 'About us',
                'verbose_name_plural': 'About us',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Client name')),
                ('description', models.TextField(verbose_name='Client say')),
                ('image', models.ImageField(default='default.png', upload_to='clients')),
            ],
        ),
        migrations.CreateModel(
            name='RecentWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Work title')),
                ('image', models.ImageField(upload_to='works')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Service name')),
                ('description', models.TextField(verbose_name='About service')),
            ],
        ),
    ]
