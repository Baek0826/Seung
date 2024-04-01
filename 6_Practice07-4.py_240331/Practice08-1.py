money=10000
while True:
  print(f'현재 {money}원이 있습니다.')
  if money== 0:
    break
  spend=int(input('사용할 금액 입력 >>>'))
  if spend<=0:
    print('0 이하의 금액은 사용할 수 없습니다.')
  elif spend>money:
    print(f'{spend-money}원이 부족합니다.')
  else:
    money-=spend