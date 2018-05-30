import os
def find(x,y):
         for q,w,e in os.walk(y):
             if x in e:
                  return os.path.join(x,q)
x = input("Enter the file name you wish to search: ")
print ("Searching the location of:", x)
print  (find(x, "C:\\"))