# Generated by Django 2.0.5 on 2018-06-17 21:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('film', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='YingPingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='发布时间')),
                ('zan', models.IntegerField(verbose_name='点赞数')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='film.Info', verbose_name='所属电影')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '影评',
                'verbose_name_plural': '影评',
            },
        ),
    ]