no=int(input('4자리 사원번호를 입력하세요. >>>'))

number=no%10
result ='오전' if number>=5 else '오후'

print(f'근무 시간은 {result}입니다.')