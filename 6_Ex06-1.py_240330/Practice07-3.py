basket=[]
count =int(input('몇 개의 과일을 보관할까요? >>>'))
for i in range(count):
  fruit = input(f'{i+1}번째 과일 이름을 입력하세요 >>>')
  basket.append(fruit)
  
print(f'입력받은 과일들은 {basket}입니다.')