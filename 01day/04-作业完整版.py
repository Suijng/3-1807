l=[]
d={}
user=input('请输入用户名:')
d['user']=user
psw=input('请输入密码:')
d['psw']=psw
cc=0
data=user+str(psw)+str(cc)
with open('data.text','a+') as f:
    f.write(data)
l.append(d)
print(l)
print('')

for i in range(3):
    name=input('请输入登录用户:')
    mm=input('请输入密码:')
    if d['user']==name and d['psw']==mm:
        print('登录成功')
        break
    else:
        print('密码或账号有误名重新输入')
        print('')