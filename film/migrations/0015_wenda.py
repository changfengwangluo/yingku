# Generated by Django 2.0.6 on 2018-07-07 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0014_huaxu'),
    ]

    operations = [
        migrations.CreateModel(
            name='WenDa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.CharField(default='', max_length=255, verbose_name='所属电影')),
                ('wen', models.CharField(default='', max_length=255, verbose_name='问题')),
                ('da', models.TextField(default='', max_length=255, verbose_name='回答')),
            ],
            options={
                'verbose_name': '电影问答',
                'verbose_name_plural': '电影问答',
            },
        ),
    ]
