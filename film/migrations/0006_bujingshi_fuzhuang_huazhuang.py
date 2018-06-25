# Generated by Django 2.0.5 on 2018-06-25 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0005_auto_20180625_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuJingShi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.CharField(default='', max_length=255, verbose_name='所属电影')),
                ('name', models.CharField(default='', max_length=255, verbose_name='中文名')),
                ('ename', models.CharField(default='', max_length=255, verbose_name='英文名')),
                ('shenfen', models.CharField(default='', max_length=255, verbose_name='身份')),
            ],
            options={
                'verbose_name': '布景师',
                'verbose_name_plural': '布景师',
            },
        ),
        migrations.CreateModel(
            name='FuZhuang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.CharField(default='', max_length=255, verbose_name='所属电影')),
                ('name', models.CharField(default='', max_length=255, verbose_name='中文名')),
                ('ename', models.CharField(default='', max_length=255, verbose_name='英文名')),
                ('shenfen', models.CharField(default='', max_length=255, verbose_name='身份')),
            ],
            options={
                'verbose_name': '服装设计',
                'verbose_name_plural': '服装设计',
            },
        ),
        migrations.CreateModel(
            name='HuaZhuang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.CharField(default='', max_length=255, verbose_name='所属电影')),
                ('name', models.CharField(default='', max_length=255, verbose_name='中文名')),
                ('ename', models.CharField(default='', max_length=255, verbose_name='英文名')),
                ('shenfen', models.CharField(default='', max_length=255, verbose_name='身份')),
            ],
            options={
                'verbose_name': '化妆',
                'verbose_name_plural': '化妆',
            },
        ),
    ]
