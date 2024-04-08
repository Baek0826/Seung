# print('show','python','is','nice')

def show(*args):
  print(' '.join(args))

# show('python','is','nice','!')
# show()

def show_kwargs(**kwargs):
  print(kwargs)

show_kwargs(a=1,b=2,c=3,d=4)