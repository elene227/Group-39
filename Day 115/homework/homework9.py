# 11) რიცხვების სიიდან "nums = list(range(1, 21))" შექმენით ახალი სია კვადრატებით, ჯერ "for"-ით, შემდეგ list comprehension-ით. შემდეგ სცადეთ მსგავსი მაგალითი სხვა მოქმედებით



nums = list(range(1, 22)) # print(list(range(1,22)))
print(nums)

sq = []
for num in nums:
    sq.append(num ** 2)
print(sq)


s = []
for i in nums:
    s.append(i * 2)
print(s)


print([i**2 for i in nums])
