s1=set()
print(type(s1))

s1.add(1)
s1.add(2)
s1.add(3)
s1.add(3)
s1.add(3)
s1.add(3)
s1.add(3)
print('s1 :',s1)

s2={3,4,5,6}
print('s2 :',s2)

print('교집합 :',s1&s2)
print('교집합 :',s1.intersection(s2))

print('합집합 :',s1|s2)
print('합집합 :',s1.union(s2))

print('차집합 :',s1-s2)
print('차집합 :',s1.difference(s2))
print('차집합 :',s2-s1)
print('차집합 :',s2.difference(s1))