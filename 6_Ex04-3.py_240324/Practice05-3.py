num1=int(input('정수1 입력 >>> '))
num2=int(input('정수2 입력 >>> '))
num3=int(input('정수3 입력 >>> '))

if num1>=num2 and num1>=num3:
  print(f'가장 큰 수는 {num1}입니다.')
elif num2>=num3:
  print(f'가장 큰 수는 {num2}입니다.')
else:
  print(f'가장 큰 수는 {num3}입니다.')

# print(f'가장 큰 수는 {max(num1, num2, num3)}입니다.')