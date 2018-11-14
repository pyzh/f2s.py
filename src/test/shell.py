from ff.models import People as p, Msg as m

def t1(): # 测试ORM
    a = p.object.all
    before = a()
    p1=p(name='tom')
    p1.save()
    after = a()
    return [before,after]


