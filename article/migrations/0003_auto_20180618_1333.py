# Generated by Django 2.0.5 on 2018-06-18 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20180618_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='yingpinginfo',
            name='laiyuan',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='来源'),
        ),
        migrations.AlterField(
            model_name='yingpinginfo',
            name='user',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='yingpinginfo',
            name='zan',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='点赞数'),
        ),
    ]