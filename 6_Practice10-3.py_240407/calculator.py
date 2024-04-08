def calculator(*args):
  sum_nums=sum(args)
  len_nums=len(args)
  max_nums=max(args)
  min_nums=min(args)
  return sum_nums,len_nums,max_nums,min_nums

# result=calculator(1,2,3,4,5)
# print(result)
sum_result,len_result,max_result,min_result=calculator(1,2,3,4,5,6,7,8,9)
print('합계 :',sum_result)
print('개수 :',len_result)
print('최대값 :',max_result)
print('최소값 :',min_result)
