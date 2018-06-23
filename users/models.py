from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.

class UserProfile(AbstractUser):

    head=models.ImageField(verbose_name='头像',upload_to='media/%Y/%m/%d',default='')
    phone=models.CharField(verbose_name='手机号',max_length=11,default='')

    class Meta:
        verbose_name='用户'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.phone

