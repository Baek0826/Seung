names=['김일남','김이남','김삼남']
ages=[99,98,97]

# for idx, name in enumerate(names):
#   print(f'{name} 아저씨는 {ages[idx]}세입니다.')

for name, age in zip(names, ages):
  print(f'{name} 아저씨는 {age}세입니다.')
  # print(item)