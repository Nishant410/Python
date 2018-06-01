#This script aims at taking an input from the user and giving the output
# as a combination of first two and last two character of the string given
#  as input
import sys

def both_ends(string):
  if len(string) > 2:
    print (len(string))
    a = (string[0]+string[1]+string[-2]+string[-1])
    print ('the final string is: ' + str(a))
  else:
    print ('there is nothing to print')
string=str(input('enter a string:'))
both_ends(string)


#from Number_reverse import func1
#func1(1,2)
#print(__name__)
