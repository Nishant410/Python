# Print string in reverse order using for loop

a=input("Enter a string: ")
z=""
for i in range (0,len(a)):
    y=a[len(a) -1 -i]
    z=z+y
print(z)
