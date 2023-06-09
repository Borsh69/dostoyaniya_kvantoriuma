# Generated by Django 4.2 on 2023-05-12 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=11)),
                ('name', models.CharField(max_length=80)),
                ('size', models.CharField(max_length=11)),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=400)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('price', models.IntegerField()),
                ('stock', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=200)),
                ('teacher', models.CharField(max_length=40)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('rank', models.IntegerField()),
                ('login', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('request_buy', models.CharField(max_length=999)),
                ('score', models.IntegerField()),
                ('size', models.CharField(max_length=10)),
            ],
            options={
                'unique_together': {('email', 'teacher', 'login', 'password', 'age', 'name')},
            },
        ),
    ]
