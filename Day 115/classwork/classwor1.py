



# nums = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

nums = []
for i in range(22):
    nums.append(i)
print(nums)

print([i for i in range(22)])


sq = []
for i in range(1, 11):
    sq.append(i*i)
print(sq)

print([i*i for i in range(1,11)])


even = []
for i in range(20,41):
    if i % 2 == 0:
        even.append(i)
print(even)

print([i for i in range(20, 41) if i % 2 ==0])

nums = [1,2,3,4,5,6,7,8,9, 10]
two = []
for i in nums:
    if i % 2 != 0:
        two.append(i*2)
print(nums)



numss = [1,2,3,4,5,6,7,8,9, 10]

print([i*2 for i in numss if i % 2!=0])