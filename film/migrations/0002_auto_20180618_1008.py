# Generated by Django 2.0.5 on 2018-06-18 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='honorcategory',
            options={'verbose_name': '电影奖名称', 'verbose_name_plural': '电影奖名称'},
        ),
        migrations.AddField(
            model_name='role',
            name='fengmian',
            field=models.ImageField(default='', upload_to='media/%Y/%m/%d', verbose_name='角色封面'),
        ),
    ]