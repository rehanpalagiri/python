def mon (a):
    if a==2:
        return 28
    elif a==4 or a==6 or a==9 or a==11:
        return 30
    return 31
testMonth = 9
s= mon (testMonth)
print("Month ", testMonth, " has: ", s, " days") 


def grade (a):
    if a>= 90:
        return "A"
    elif a>=80 and a<=89: 
        return "B"
    elif a>=70 and a<=79: 
        return "C"
s= grade (79)
print("what is my grade: ",s)



