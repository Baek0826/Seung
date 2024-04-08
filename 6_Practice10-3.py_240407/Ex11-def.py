#인수:없음, 반환값:없음
def make_num():
  a=1
  print(a)

result=make_num()
print(result)

#인수:없음, 반환값:있음
def get_num():
  a=1
  # print(a)
  return a

result=get_num()+get_num()
print(result)

#인수:있음, 반환값:없음
def show_num(a,b):
  print(a+b)

print(show_num(20,30))

#인수:있음, 반환값:있음
def add_num(a,b):
  result=a+b+1
  return result

print(add_num(200,300)+add_num(200,300)+add_num(200,300))