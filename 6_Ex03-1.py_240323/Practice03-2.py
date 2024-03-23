days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#print(len(days))
month=int(input('1~12 사이의 월을 입력하세요 >>>'))
day=days[month-1]

print(f'{month}월 {day}일까지 있습니다.')