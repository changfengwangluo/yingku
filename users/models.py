from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    head=models.ImageField(verbose_name='头像',upload_to='media/%Y/%m/%d',null=True,blank=True)
    phone=models.CharField(verbose_name='手机号',max_length=11,null=True,blank=True)

    class Meta:
        verbose_name='用户'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.user.username

