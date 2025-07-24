# 7) დაწერეთ ფუნქცია tuple_info, რომელიც მიიღებს tuple-ს და დაბეჭდავს მის სიგრძეს, პირველ და ბოლო ელემენტს

def tuple_info(t):
    leng = 0
    for i in t:
        leng += 1

    # *a, last = t
    # first, *a = t 
    first, *a, last = t 
    return (leng, first, last)




print(tuple_info((1,2,3,4,5,6,7,8)))
    
