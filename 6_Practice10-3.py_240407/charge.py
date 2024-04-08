def charge(energy):
  max_charge=100
  current_charge=0
  while True:
    print(f'현재 충전상태는 {current_charge}입니다.')
    current_charge+=energy

    if(current_charge>max_charge):
      return

charge(10)