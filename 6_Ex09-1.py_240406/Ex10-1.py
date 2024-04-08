while True:
  p=input('하이픈을 포함한 전체 주민등록번호를 입력하세요 >>>')
  # print(p.find('-'))
  
  # index는 찾는 값이 없으면 실행x
  # if p.index('-')!=6:
  #   print('하이픈의 위치가 잘못되었습니다.')
  #   continue
  
  if p.find('-')!=6:
    print('하이픈의 위치가 잘못되었습니다.')
    continue
  birthday=p.split('-')[0]
  print(f'생년월일은 {birthday}입니다.')
  break