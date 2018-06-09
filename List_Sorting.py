# Take user input as strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first

a=[]
c=[]
for i in range(0,6):
    i=input('enter a string: ')
    if i[0]=='x':
        c.append(i)
        c.sort()
    else:
      a.append(i)
      a.sort()
print(c+a)