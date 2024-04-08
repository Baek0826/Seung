exam=[]
print('점수를 입력하세요. 더 이상 입력할 점수가 없으면 음수를 아무거나 입력하세요.')
while True:
  score=int(input('점수 입력 >>>'))
  if score<0:
    break
  else:
    exam.append(score)
average=sum(exam)/len(exam)
maximum=max(exam)
minimum=min(exam)
print(f'평균 = {average} 최대 = {maximum} 최소 = {minimum}')
