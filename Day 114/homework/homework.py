# 2) შექმენით ფუნქცია manual_index, რომელიც მიიღებს სიას და ელემენტს და დააბრუნებს ელემენტის ინდექსს სიაში. გამოიყენეთ მხოლოდ loop და if, .index მეთოდის გარეშე


def manual_index(lst, elemen):
    return [i for i in range(len(lst)) if lst[i] == elemen]

print(manual_index([15,17,19,27], 15))
