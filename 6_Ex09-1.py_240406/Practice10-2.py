no=input('사업자 등록번호를 입력하세요(예: 123-45-67890) >>>')

# no='123-45-67890'

case=len(no)==12
case2=no.find('-')==3
case3=no.rfind('-')==6
case4=no.replace('-','').isdecimal()
if case and case2 and case3 and case4:
  print('올바른 형식입니다.')
else:
  print('올바른 형식이 아닙니다.')