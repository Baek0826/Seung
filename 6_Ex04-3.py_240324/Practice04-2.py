times=int(input('초를 입력하세요 >>>'))

hour=(times//3600)
minute=(times%3600//60)
second=(times%60)

print(f"변환 결과는 {hour}시간 {minute}분 {second}초입니다.")