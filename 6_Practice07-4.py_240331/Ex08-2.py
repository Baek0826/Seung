hobbies=set()
while True:
  hobby=input('취미를 입력하세요 >>>')
  if hobby=='':
    print('입력된 취미가 모두 저장되었습니다.')
    break
  else:
    hobbies.add(hobby)
print(hobbies)