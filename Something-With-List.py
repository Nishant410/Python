#This script will take user input to create a list of strings,  and will check
# if the elements are of 2 or more characters. If it states true and their
# first and last characters are same, then it will put them in a new list
# and give the count of such strings.

z=[]
y=[]
for i in range(0,5):
    i=input('Enter a string:')
    if len(i) >= 2 and i[0]==i[-1]:
      y.append(i)
    z.append(i)
print ("")
print ('User\'s Final list is: ', z)
print ("")
print ('List prepared by script is: ', y)
print ("")
print('Number of strings that met the script\'s condition: ', len(y))


