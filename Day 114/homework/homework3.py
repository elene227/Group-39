#5) დაწერეთ ფუნქცია, რომელიც მიიღებს სიას და დაბეჭდავს უნიკალურ ელემენტებს და მათ რაოდენობას სიაში, მაგ: apple - 2, banana - 3... გამოიყენეთ .count მეთოდი



# def single_element(lst):
#     for i in (lst):
#         if lst.count(i) > 0:
#             print (f"{i} - {lst.count(i)}")

# single_element(["apple","apple","orange","lemon","Blueberries","pie","lemon","pie","orange"])
        

# def single_element(lst):
#     return [f"{i} - {lst.count(i)}" for i in lst if lst.count(i)> 0]#[0]

# print(single_element(["apple","apple","orange","lemon","Blueberries","pie","lemon","pie","orange"]))


# def single_element(lst):
#     for i in set(lst):
#         print(f"{i} - {lst.count(i)}")

# single_element(["apple","apple","orange","lemon","Blueberries","pie","lemon","pie","orange"])


def single_element(lst):
   un = set(lst)
   for i in un:
       print(f"{i} - {lst.count(i)}")
       
single_element(["apple","apple","orange","lemon","Blueberries","pie","lemon","pie","orange"])



      
    
      

