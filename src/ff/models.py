from django.db import models as m
from functools import partial as p

# void = lambda *a,**kw:None
# F = lambda x,*a,y='',**kw: void(x,*a,z=y,**kw) 
M=m.Model
t = lambda 长=12,_='',**kw: m.TextField(max_length=长,**kw); txt=T=t
c = lambda 长=12,_='',**kw: m.CharField(max_length=长,**kw); char=c
ref = lambda src,*a,**kw: m.ForeignKey(src,*a,on_delete=m.CASCADE,**kw)
dt =  lambda txt,*a,**kw: m.DateTimeField(txt,*a,**kw)
n = lambda default=0,**kw: m.IntegerField(default=default,**kw)

class People(M):
    name = c(24); url_id = c(36)
    base = c(12,'所在地')
    type = n(0) # -1为女
    url = c(360,'网址');  bio = t(1080)
    email = c(64); code = c(128)

    def __str__(e):
        return e.name


class Msg(M): #= status
    url_id = c(36)
    context = t(140);  p = ref(People)
    time = dt('时间')

    def __str__(e):
        return ''+e.url_id+' '+time



