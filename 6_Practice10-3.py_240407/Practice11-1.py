def vending_machine(money):
  price=700
  count=money//700
  for drink in range(count+1):
    change=money-drink*price
    print(f'음료수 = {drink}개, 잔돈 = {change}')
  
vending_machine(3000)