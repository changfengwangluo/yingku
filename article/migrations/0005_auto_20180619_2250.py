# Generated by Django 2.0.5 on 2018-06-19 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_huaxuinfo_keywords_yingxuninfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keywords',
            name='words',
            field=models.CharField(max_length=255, unique=True, verbose_name='关键词'),
        ),
    ]