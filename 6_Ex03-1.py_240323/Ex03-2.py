print('python','java','c',sep=',')
print()
print('영화 타이타닉')
print('평점',end=':')
print('5점')

fos=open('sample.py','w') #wt:write text
print('print(\'hello python!\')', file=fos)
fos.close()