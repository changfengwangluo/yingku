# Generated by Django 2.0.5 on 2018-06-17 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LunBo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media/%Y/5m/%d', verbose_name='图片')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('desc', models.CharField(max_length=255, verbose_name='描述')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
    ]