#16) სთხოვეთ მომხმარებელს შეიყვანოს რიცხვი "input()"-ით და გადააკეთეთ "int"-ად. გამოიყენეთ "try" და "except", რომ გაუმკლავდეთ შეცდომას თუკი სიმბოლოები შეიყვანეს. დაბეჭდეთ „შეიყვანეთ მხოლოდ რიცხვი“




try:
    user = int(input("please enter a number: "))
except ValueError:
    print("only nums no symbols!")
