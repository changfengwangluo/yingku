from django.db import models

# Create your models here.


class Info(models.Model):
    name=models.CharField(verbose_name='歌曲名',max_length=255)

    class Meta:
        verbose_name='影乐'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name