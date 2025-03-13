a=int(input("enter a number:"))
b=int(input())
c=int(input())
if(a<b and a<c):
    print(a,"is smaller number")
elif(b<a and b<c):
    print(b,"is smaller number") 
elif(c<b and c<a):
    print(c,"is smaller number")   
elif(a==b and b==c):
    print(a,b,c,"are smaller and equal numbers")
elif(a==b and a<c):
    print(a,b"are smaller and equal numbers")
elif(b==c and b<a):
    print(b,c,"are smaller and equal numbers") 
elif(a==c and c<b):
    print(a,c,"are smaller and equal numbers")    
