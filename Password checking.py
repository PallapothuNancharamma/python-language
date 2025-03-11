pass_word=str(input("enter string"))
b=len(pass_word)
digit=False
upper=False
lower=False
if b<8:
    print("Ivalid password")
for i in pass_word:
    if(i.isupper()):
        upper=True
    elif(i.islower()):
        lower=True    
    elif(i.isdigit()):
        digit=True 
if(digit and upper and lower) :
    print("Valid password")
else:
    print("Invalid password: Password must be at least 8 characters long.")
    
