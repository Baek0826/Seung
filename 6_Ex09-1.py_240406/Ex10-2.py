# a_list=['above','cookie','app','about','admin','bisket','apple','april']
a_list=['aaa','bbb','ccc','ddd']
for item in enumerate(a_list):
  index, item=item
  # print(index, item)
  if item.find('a')==-1:
    result=a_list.pop(index)
    print(f'{result} 제거됩니다.')
print(a_list)