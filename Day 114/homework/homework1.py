#3) შექმენით ფუნქცია manual_count, რომელიც მიიღებს სიას და ელემენტს და დააბრუნებს ელემენტის რაოდენობას სიაში. გამოიყენეთ მხოლოდ loop და if, .count მეთოდის გარეშე


def manual_count(lst, elm):
    countt = 0
    for i in lst:
        if i == elm:
            countt += 1
    return countt


#1)def manual_count(lst, elm):
#     return len([i for i in lst if i == elm])

# print(manual_count([5,6,5,6,7,8], 1))


#2)def manual_count(lst, elm):
#     return 0 if not lst else(1 if lst[0]== elm else 0)

# print(manual_count([4,4,4,1,2,78,9], 4))

#3)def manual_count(lst, elm):
    # return sum([1 for i in lst if i == elm])