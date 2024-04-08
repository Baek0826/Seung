# a_list=['above','cookie','app','about','admin','bisket','apple','april']
a_list=['aaa','bbb','ccc','ddd']
i=0
while True:
  try:
    if a_list[i].find('a')==-1:
      print(f'{a_list.pop(i)} 제거됩니다.')
    else:
      i+=1
  except:
    break

print(a_list)