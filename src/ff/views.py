from use.v import render
# from .models import M
# from .models import Msg:M
from .models import Msg

def 目录(req): # 随便看看
    result = Msg.objects.all()[:25]
    return render(req, '主页.htm',{'msg':result})



