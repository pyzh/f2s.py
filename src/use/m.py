from django.db import models as m


# void = lambda *a,**kw:None
# F = lambda x,*a,y='',**kw: void(x,*a,z=y,**kw) 
M=m.Model
t = lambda 长=12,_='',**kw: m.TextField(max_length=长,**kw); txt=T=t
c = lambda 长=12,_='',**kw: m.CharField(max_length=长,**kw); char=c
ref = lambda src,*a,**kw: m.ForeignKey(src,*a,on_delete=m.CASCADE,**kw)
dt =  lambda txt,*a,**kw: m.DateTimeField(txt,*a,**kw)
n = lambda default=0,**kw: m.IntegerField(default=default,**kw)
