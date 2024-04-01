pw='qwerty'
count=5
while True:
  if count==0:
    print('비밀번호 입력 횟수를 초과했습니다.')
    break
  pw_input=input('비밀번호를 입력하세요 >>>')
  if pw_input==pw:
    print('비밀번호를 맞혔습니다.')
    break
  count-=1