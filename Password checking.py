pass_word=str(input("enter the password:"))
b=len(pass_word)
digit=False
upper=False
lower=False
character=False
special_character = {'!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'}
if b<8:
    print("Invalid password: Password must be at least 8 characters long.")
for i in pass_word:
    if(i.isupper()):
        upper=True
    elif(i.islower()):
        lower=True    
    elif(i.isdigit()):
        digit=True
    if i in special_character:
        character=True
        
if(digit and upper and lower and character) :
        print("Valid password")
else:
    print("Invalid password: Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
