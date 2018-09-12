import re
l=[]
print('         注册信息账户')
print('')

while True:
    d={}
    print('用户名只能是字母和数字')
    user=input('请输入用户名:')
    print('密码为6位数字')
    psw=input('请输入密码:')
    if re.match(r'\w',user):
        d['user']=user
    elif re.match(r'\d{6}$',psw):
        d['psw']=psw
        break
    else:
        print('输入有误请重新输入')
        
l.append(d)
print(l)