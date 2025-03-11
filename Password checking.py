pass_word=str(input("enter string"))
b=len(pass_word)
digit=False
upper=False
lower=False
if b<8:
    print("Ivalid password")
for i in  range(b):
    if(pass_word[i].isupper()):
        upper=True
    elif(pass_word[i].islower()):
        lower=True    
    elif(pass_word[i].isdigit()):
        digit=True 
if(digit and upper and lower) :
    print("Valid password")
else:
    print("Invalid password: Password must be at least 8 characters long.")
    
