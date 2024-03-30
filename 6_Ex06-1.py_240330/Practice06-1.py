num=int(input('정수를 입력하세요 >>>'))

if num<=0:
  print('잘못된 입력입니다.')
else:
  n=1
  while n<=num:
    print(f'{n}번째 Hello')
    n+=1