num=1

def outer_function():
  global num
  num=2

  def inner_function():
    # nonlocal num
    global num
    num=3
    print(num)

  inner_function()
  print(num)

outer_function()
print(num)