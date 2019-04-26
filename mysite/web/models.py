from django.db import models
class douban(models.Model):
    name=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    jianjie=models.CharField(max_length=255)
    riqi=models.CharField(max_length=255)  
    jiage=models.CharField(max_length=255)
    chubanshe=models.CharField(max_length=255)
    pingfen=models.CharField(max_length=255)
class jingdong(models.Model):
    biaoti=models.CharField(max_length=255)
    jiage=models.CharField(max_length=255)
    jianjie=models.CharField(max_length=255)
