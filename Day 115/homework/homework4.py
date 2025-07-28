# 6) შექმენით ლექსიკონი person და გამოიყენეთ .items() მეთოდი, რათა დაბეჭდოთ ყველა key და value წყვილად. გამოიყენეთ loop და კომენტარი დაუმატეთ შედეგს

person = {
    "person1":"ivan",
    "person2":"martha",
    "person3":"lys",
    "person4":"luc"

}

print(person.items())

for i in person.values(): 
    print(i)
    # (: