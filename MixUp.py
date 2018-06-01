import sys

def mixup(a, b):
    x=a[0]
    y=b[0]
    z=y+a[1:]+" "+x+b[1:]
    print (z)

a = str(input('enter a string:'))
b = str(input('enter another string:'))
mixup(a,b)

def main():
    if __name__ == '__main__':
        main()