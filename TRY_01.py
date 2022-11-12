import string
def gtr():    
    s1=input("Enter first string: ")
    s2=input("Enter second string: ")
    print("str1 is:",s1)
    print("str2 is:",s2)
    print("Is",s1,"greater than",s2,"=",s1>s2)
    print("Is",s1,"less than",s2,"=",s1<s2)
    print("Is",s1,"equal to",s2,"=",s1==s2)
    print("Is",s1,"not equal to",s2,"=",s1!=s2)
    print("Is",s1,"greater than or equal to",s2,"=",s1>=s2)
    print("Is",s1,"less than equal to",s2,"=",s1<=s2)


def cpx():
    
    a=input("Enter a value:")
    b=input("Enter a value:")
    print(int(a))
    print(chr(int(a)))
    print(hex(int(a)))
    print(complex(int(a),int(b)))




def frt():
    
    x=int(input("Enter a value:"))
    print("%.2f" %x)
    print("%.6f" %x)
    y=int(input("Enter a value:"))
    print("%d" %y)
    print("%2d" %y)
    print("%3d" %y)
    print("The given number in octal form is: %o" %y)
    print("The given number in hex form is: %X" %y)






#Write a program that a year is a leap or not, take input from user.    !!!!!!!!!!!!!
#Write a program to find G.C.D of two given two numbers.    !!!!!!!!!!!!!
def fr():    
    y=int(input("Please enter a number: "))
    x=0
    i=0
    
    while (x<=y):
        if (x%2)==0:
            i+=x
        x+=1
    print("Sum:",i)

#y=int(input("Enter the year: "))
#if (y%4==0):
#    print("The given year %d is leap year" %y)

#else:
#    print("The given year %d is not leap year" %y)

def gcd():
    
    x=int(input("Enter the num1: "))
    y=int(input("Enter the num2: "))
    
    mod = 1
    
    while (mod!=0):
        mod=y%x
        gcd=x
        y=x
        x=mod
        print(gcd)

def whl():
    
    n=int(input(""))
    x=0
    while(x<n):
        x+=1
        print(x)
    
    else:
        print("While loop terminated.")


def TBL():
    x=int(input("Table of number: "))
    y=int(input("Till the count of :"))
    #z=int(input())
    if 0<=y<=20:
        for a in range (0,y+1):
            print(x,"*",a,"=",x*a)

    elif y>20:
        for a in range(21):
            print(x,"*",a,"=",x*a)
        print("Error, printing can extend till 20 only")
                
    #for a in range(1,y+1):
    #    if (a<=20):
    #        print(x,"*",a,"=",x*a)
    #else:
    #    if (y>20):
    #        print("Error")



def FZ():
    n=int(input())
    for x in range(1,n+1):
        if x%3==0 and x%5==0:
            print("FizzBuzz")
        elif x%3==0:
            print("Fizz")
        elif x%5==0:
            print("Buzz")
        else:
            print(x)

def Pi():


    x=int(input(""))
    y=float(22/7)
    for i in range (1,x):
        print("{:.{}f}".format(y,i))

#SOLVE
'''write a program to print fibonacci numbers less than a given number
    and calculates the sum all alternate number which are even positions'''


def FBC():
    n=int(input("No. of times fabonacci series to be printed: "))
    for i in range(0,n+1):
        i+=i
        print(i)
        

#Program to skip all numbers below 10 and maximum range should be 20
def CN():
    
    for a in range(0,21):
        if a<10:
            continue
        print(a)
def CN2():
    s=input("Enter any string: ")
    l=len(s)
    for a in s:
        if a=='e':
            continue
        print(a)
def PS():
    l1=[2,4,3,2,9,14,23]
    for a in l1:
        if a%2!=0:
            pass
        else:
            print(a,"= Even Number")
    
def CN3():
    x=int(input("Lower range: "))
    y=int(input("Upper range: "))
    for a in range(x,y+1):
        for z in range (2,a):
            if a%z==0:
                break
        else:
            print(a)

#Write a program to check wether a number is armstrong number or not.
#All single digit numbers are armstrong numbers while there are npo two digit armstrong numbers
def arm():
    x=input("Enter a number: ")
    p=len(x)
    z=0
    if 99<int(x):
        for a in range(0,p):
            d=int(x[a])**p
            z=z+d
        if int(x)==z:
            print("Armstrong number")
                
        else:
            print("Not Armstrong")

        print(z)
def lmb():
    a,b,c=int(input()),int(input()),int(input())
    x=lambda a,b,c:(a+b)**c
    print(x(a,b,c))
def lmb2():
    sal=int(input())
    tax=lambda sal:sal*20/100
    print(tax(sal))
'''
def cube(a):
    return a**3

l=[12,34,5,12,44,65]
print(l)
print(list(map(cube,l)))

print("With lambda function:",list(map(lambda a:a%2==0,l)))

print("List Compehension:",[i**4 for i in l])

print("Filter function:",list(filter(lambda a:a%2==0,l)))

print("List comprehension with filter:",[i for i in l if i%2==0])

'''

'''globvar="Evening"
def fun1():
    globvar="Good Morning"
    print(globvar)
def fun2():
    globvar="Night Night"
    print(globvar)

    
fun1()
fun2()
print(globvar)




def f(a):
    return a**2
def g(a):
    return 2*a
def h(a):
    return a+1

print(h(g(f(3))))   
'''

def str():
    a=input("str1: ")
    b=input("str2:")
    c=3*b
    print(a.capitalize())
    print(a.title())
    print(a.split())
    print(a.center(20))
    print(a.lower())
    print("@".join(a))
    print(a.replace("z","e"))
    
def str2():
    a=input("str:")
    if a.startswith("Python")==True:
        print("valide")
    else:
        print("invalid")
    print("char with min value:",min(a))
    print("char with max value:",max(a))


def str3():
    a=input("str: ")
    x=""
    for i in a:
        if i not in string.punctuation:
            x=x+i
        
    print(x)


def str4():
    a=input("str: ")
    x=""
    for i in a:
        x=x+i*2
    print(x)








