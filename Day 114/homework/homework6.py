# 8) შექმენით tuple, რომელიც შეიცავს სამ მნიშვნელობას (მაგ. სახელი, ასაკი, ქვეყანა). გამოიყენეთ tuple unpacking ამ მნიშვნელობების ცალკეულ ცვლადებში მოსათავსებლად და დაბეჭდეთ თითოეული ცვლადი


names = ("Kurt", "axl", "freddie", "David", "mick", "Robert", "Dave")
age = (27, 63, 45, 69, 81, 76, 56)
city = ("London", "New York City", "Paris", "Rome")

Cobain, Rose, Mercury, Bowie, Jagger, Plant, Grohl = names
age0, age1, age2, age3, age4, age5, age6= age
city0, city1, city2, city3 = city

print(Cobain, Rose, Mercury, Bowie, Jagger, Plant, Grohl)
print(age0, age1, age2, age3, age4, age5, age6)
print(city0, city1, city2, city3)
