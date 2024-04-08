def get_average(marks):
  # total=0
  # for subject in marks:
  #   total+=marks[subject]
  total=sum(marks.values())
  average=total/len(marks)
  return average

marks={'국어':90, '영어':80, '수학':85}
average=get_average(marks)
print(f'평균은 {average}점입니다.')