fruits=[]
count=3

while count>0:
  fruit=input('어떤 과일을 저장할까요? >>>')
  if fruit in fruits:
    print('동일한 과일이 있습니다.')
    continue
  fruits.append(fruit)
  count-=1
  print(f'입력이 {count}번 남았습니다.')

print(fruits)