student='"김철수",85'
name,score=student.split(',')
print(f'이름은 {name.strip('"')}이고, 점수는 {score}점입니다.')