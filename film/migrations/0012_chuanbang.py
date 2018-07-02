# Generated by Django 2.0.5 on 2018-07-02 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0011_auto_20180702_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChuanBang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.CharField(default='', max_length=255, verbose_name='所属电影')),
                ('xiangqing', models.CharField(default='', max_length=255, verbose_name='穿帮详情')),
            ],
            options={
                'verbose_name': '穿帮镜头',
                'verbose_name_plural': '穿帮镜头',
            },
        ),
    ]
