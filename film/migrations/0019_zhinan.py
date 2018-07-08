# Generated by Django 2.0.5 on 2018-07-08 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0018_auto_20180708_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZhiNan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.CharField(default='', max_length=255, verbose_name='所属电影')),
                ('category', models.CharField(default='', max_length=255, verbose_name='类型')),
                ('desc', models.TextField(default='', max_length=255, verbose_name='详情')),
            ],
            options={
                'verbose_name': '家长指南',
                'verbose_name_plural': '家长指南',
            },
        ),
    ]