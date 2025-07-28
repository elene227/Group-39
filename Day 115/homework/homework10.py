#12) სიიდან "mixed = [2, 5, 8, 11, 14, 17, 20]" შექმენით ორი სია list comprehension-ით: ერთში მხოლოდ ლუწები, მეორეში — კენტები



mixed = [2, 5, 8, 11, 14, 17, 20]


list1 = []
for i in mixed:
    if i % 2 == 1:
        list1.append(i)
print(list1)


list1 = [i for i in mixed if i & 2 == 0]
print(list1)