from django.shortcuts import render
from web.models import douban,jingdong

def doubanindex(request):
    db_list=douban.objects.all()
    return render(request,'douban.html',{'db_list':db_list})
def jdindex(request):
    jd_list=jingdong.objects.all()
    return render(request,'jingdong.html',{'jd_list':jd_list})