a_list=['above','cookie','app','about','admin','bisket','apple','april']
# a_list=['aaa','bbb','ccc','ddd']
new_a_list=[]
while a_list:
  item=a_list.pop(0)
  if item.find('a')>=0:
    new_a_list.append(item)
  else:
    print(f'{item} 제거됩니다.')
print(new_a_list)