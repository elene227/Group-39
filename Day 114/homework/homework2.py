# 4) შექმენით სიები fruits, colors, numbers. თითოეულზე გამოიყენეთ index, count, sort, sorted, min, max მეთოდები & ფუნქციები და დააკომენტარეთ თითოეული მაგალითი (რას აკეთებს)

fruits = ["Blueberries","peaches", "Lemon", "orange","cranberries<3"]
colors = ["Grey", "Blue", "purple", "white","black", "pink",]
numbers = [19, 94, 22, 21, 21.5, 5.1, 27]

print(fruits.index('Lemon'))

print(colors.count("Grey"))

numbers.sort()
print(numbers)

sortd = sorted(fruits) # it doesnt chnage list remains unchanged.
print(sortd)

print(min(numbers))
print(max(numbers))

# print(numbers.insert(0, 17)) this returns value of insert its always None. wont work.
# instead write insert itself then use print <:
numbers.insert(0, 17)
print(numbers)