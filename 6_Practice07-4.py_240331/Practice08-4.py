for dan in range(2, 10):
  if dan%2==0:
    continue
  for n in range(1,10):
    if n>dan:
      break
    # if dan%2==0:
    #   break
    print(f'{dan}×{n}={dan*n}')
  print()