print("Pycalc v 2.0 by tfilipp")
print ("loading...")
a=0
b=1
c1=a+b
c2=a-b
c3=a*b
c4=a/b
c5=a//b #целая часть от деления
c6=a%b #остаток от деления
c7=a**b
print("Done. Changing to russian and resetting values...")
a=0
b=0
while True:
    a=int(input("Input first number: "))
    o=input("""What to do?
    Type operators >>>""")
    b=int(input("Input second number: "))
    print("Calculating...")
    c1=a+b
    c2=a-b
    c3=a*b
    c4=a/b
    c5=a//b #целая часть от деления
    c6=a%b #остаток от деления
    c7=a**b
    print ("Done.")
    if (o=="+"):
        print (c1)   
    elif (o=="-"):
        print (c2)
    elif(o=="*"):
        print(c3)
    elif(o=="/"):
        print(c4)
    elif(o=="/%"):
        print (c5, c6)
    elif(o=="=="):
        if (a>b):
            print(a,">", b)
        elif (a<b):
            print(a, "<", b)
        else:
            print(a,"=",b," or null")
    elif(o=="**"):
        print(c7)
    elif(o=="create c17"):
        print(c1, c2, c3, c4, c5, c6, c7)
    elif(o=="create c1 7"):
        print("+ ",c1," - ", c2," * ", c3," / ", c4," /%:", c5," <whole", c6," <bypass **>", c7)
    else:
        print("ERR_NO_OPERATORS")
    print ("result printed.")
