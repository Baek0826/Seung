pwd='12344'

ch_count=0
num_count=0

for ch in pwd:
  if ch.isalpha():
    ch_count+=1
  if ch.isnumeric():
    num_count+=1

if ch_count>0 and num_count>0:
  print('사용 가능한 비밀번호입니다.')
else:
  print('불가능한 비밀번호입니다.')