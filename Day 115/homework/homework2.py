#4) შექმენით dictionary სახელად student, დაამატეთ მას მონაცემები: name, hobby, height, weight. შემდეგ გამოიყენეთ .get() მეთოდი name-ის მისაღებად და .pop() მეთოდი height-ის წასაშლელად. დაუმატეთ კომენტარები, რას აკეთებს თითოეული მეთოდი

student = {
    "name": "your name",
    "hobby": "your hobby",
    "height": "your height",
    "weight": "your weight"

}

print(student.get("name")) # ტერმინალში გამოაქ ნეიმის მნიშვნელობა 
print(student.pop("height")) # შლის მნიშვნელობას height ის (Key თი უნდა მიწვდე მნიშვნელობას)
