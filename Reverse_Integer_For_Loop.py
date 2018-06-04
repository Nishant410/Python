a=input("Enter an Integer: ")
b=str(a)
z=""
for i in range (0,len(b)):
    y=b[len(b) -1 -i]
    z=z+y
print(z)