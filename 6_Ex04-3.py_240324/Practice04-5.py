kor=int(input('국어 점수를 입력하세요. >>>'))
eng=int(input('영어 점수를 입력하세요. >>>'))
math=int(input('수학 점수를 입력하세요. >>>'))

avg=(kor+eng+math)/3

result='합격' if avg>=80 else '불합격'

print(f'평균은 {avg}점이고, 결과는 {result} 입니다.')