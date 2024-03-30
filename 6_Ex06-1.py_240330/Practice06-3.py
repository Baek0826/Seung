coffee= 0
money=int(input('자판기에 얼마를 넣을까요? >>>'))

while money>=300:
  money-=300
  coffee+=1
  print(f'커피 {coffee}잔, 잔돈{money}원')
