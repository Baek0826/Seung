my_list=['a','b','c']
print(my_list)

your_list=['d','e','f']
print('my_list+your_list :', my_list+your_list)
print('my_list :', my_list)

my_list.extend(your_list)
print('extend() :', my_list)

my_list.remove('b')
print('remove() :', my_list)