#13) სიიდან "animals = ['tiger', 'lion', 'zebra', 'elephant', 'giraffe']" შექმენით ახალი სია, რომელიც შეიცავს სიტყვების პირველ ასოებს, ჯერ "for"-ით, შემდეგ list comprehension-ით. შემდეგ აირჩიეთ მხოლოდ ის სიტყვები, რომლებიც "e"-ზე იწყება



animals = ['tiger', 'lion', 'zebra', 'elephant', 'giraffe']


fr = []
for i in animals:
    fr.append(i[0])
print(fr)


fr = [i[0] for i in animals]
print(fr)



fr = [i for i in animals if i[0]== "e"]
print(fr)