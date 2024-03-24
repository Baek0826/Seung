important=40

# if important>=100:
#   print('상')
# else:
#   if important>=50:
#     print('중')
#   else:
#     print('하')

if important>=100:
  print('상')
elif important>=80:
  print('상중')
elif important>=50:
  print('중')
elif important>=30:
  print('중하')
else:
  print('하')