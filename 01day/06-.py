import re 
def wo():
    age=input('请输入年龄:')

def ni(a):
    ret=re.match(r'\d',a)
    if ret:
        print('对的')
    else:
        print('')
a=wo()
a