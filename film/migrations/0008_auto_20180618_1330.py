# Generated by Django 2.0.5 on 2018-06-18 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0007_auto_20180618_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='fengmian',
            field=models.ImageField(default='', upload_to='image/%Y/%m/%d', verbose_name='角色封面'),
        ),
    ]