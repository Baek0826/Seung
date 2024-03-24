car_no=input('차량번호를 입력하세요. >>>')

if int(car_no[-1])%2==0:
  result= '운행가능'
else:
  result= '운행불가'

print(f'차량번호 {car_no}는 오늘 {result}입니다.')