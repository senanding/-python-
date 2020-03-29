from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class formalVIP(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    nick=models.CharField(blank=True,max_length=50)
    birthday=models.DateField(blank=True,null=True)
    class Meta:
        verbose_name_plural="普通会员表"#指定模型的复数形式