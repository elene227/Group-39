#7) შექმენით ლექსიკონი animal, შექმენით მისი ასლი .copy() მეთოდით, შემდეგ კი გამოიყენეთ .clear() ორივეზე (დასაწყისში და ბოლოს დაბეჭდეთ ორივე ლექსიკონი, კომენტარით)

animal ={
    "animal1":"cat",
    "animal2":"DAWG",
    "animal3":"parrot"

}

co = animal.copy()
print(co)

co.clear()
print(co)
animal.clear()
print(animal)