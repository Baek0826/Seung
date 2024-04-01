for i in range(1, 100):
  left=i//10
  right=i%10
  
  case_left=left%3==0 and left!=0
  case_right=right%3==0 and right!=0

  if case_left and case_right:
    result='짝짝'
  elif case_left or case_right:
    result='짝'
  else:
    result=i
  if i%10==0:
    print(result)
  else:
    print(result, end='\t')