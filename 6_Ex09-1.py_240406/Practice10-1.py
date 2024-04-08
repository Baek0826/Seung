phone=input('전화번호를 입력하세요 >>>')

#split
# code=phone.split('-')[1]
# print(code)

#index
start=phone.index('-')+1
end=phone.index('-',start)
# print(start)
# print(end)
code=phone[start:end]
print(code)

#find
start=phone.find('-')+1
end=phone.find('-',start)
# print(start)
# print(end)
code=phone[start:end]
print(code)