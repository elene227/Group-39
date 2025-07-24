# 10) შექმენით set სახელად numbers, დაამატეთ მას ორი რიცხვი add() მეთოდით და წაშალეთ ორი ელემენტი remove() მეთოდით. შემდეგ შექმენით მეორე set სახელად even_numbers და გამოიყენეთ union(), intersection(), difference() ორივე set-ზე. დაუმატეთ კომენტარები, რას აკეთებს თითოეული მეთოდი



numbers = set()

numbers.add(2)
numbers.add(4)

numbers.add(2)
numbers.add(4)

numbers.add(2)
numbers.add(4)
numbers.add(6)

even_numbers = {2,4,6,2,4,8}

print(even_numbers.union(numbers)) # აერთიანებს იმ ელემენტებს და ამაყებს იმ ელემენტებს რომლებიც არ არის even number ში

print(even_numbers.intersection(numbers)) # პრინტავს იმ ელემენტებს რომლებიც ორივეშია

print(even_numbers.difference(numbers)) # პრინტავს იმ რიცხვებს რომელიც მხოლოდ პირველ სეთშია





















































# i want pieeeee