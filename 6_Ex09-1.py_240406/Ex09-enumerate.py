list=['가위','바위','보']

# print('가위바위보 게임 1회 : 가위')
# print('가위바위보 게임 2회 : 바위')
# print('가위바위보 게임 3회 : 보')

# count=1
# for item in list:
#   print(f'가위바위보 게임 {count}회 : {item}')
#   count+=1

# for item in enumerate(list):
#   # print(item)
#   print(f'가위바위보 게임 {item[0]+1}회 : {item[1]}')

for index, item in enumerate(list):
  # print(item)
  print(f'가위바위보 게임 {index+1}회 : {item}')