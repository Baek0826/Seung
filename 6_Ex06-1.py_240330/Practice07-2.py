sum_num=0
num=int(input('임의의 양수를 입력하세요 >>>'))
for n in range(1,num+1):
  sum_num+=n
print(f'1부터 {num}사이의 모든 정수의 합계는 {sum_num}입니다.')
