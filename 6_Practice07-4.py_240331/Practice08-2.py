while True:
  movie=int(input('이번 영화의 평점을 입력하세요 >>>'))
  if movie>5 or movie<=0:
    print('평점은 1~5 사이만 입력할 수 있습니다.')
  else:
    print(f'평점: {'★ ' * movie}')
    break