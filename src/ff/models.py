
from use.m import *

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

   #  def __str__(e):
    #    return ''+e.url_id+' '+e.time



