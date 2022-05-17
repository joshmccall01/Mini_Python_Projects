'''

Without using complex math module:

Program to take any real quadratic equation in the form ax**2+bx+c=0 
and return the roots x1 and x2 to 2 decimal places

- Josh McCall
'''

import math

def main():
    print("This is a program to give the roots of a quadratic equation of the form: ax^2+bx+c=0 where a,b and c are real")
    #taking input values
    a= float(input("What is the a value?"))
    b= float(input("What is the b value?"))
    c= float(input("What is the c value?"))

    #calculating discriminant

    dis = b**2-4*a*c

    #case 1: when both roots are real1

    if dis>0:
        x1= round((-b+math.sqrt(dis))/(2*a), 2)
        x2= round((-b-math.sqrt(dis))/(2*a), 2)
        return(print("x1=",x1, "x2=",x2))

    #case 2: repeated root

    elif dis==0:
        x=round(-b/(2*a), 2)
        return(print("Repeated root: x=", x))

    #case 3: imaginary roots

    else:
        #calculating the real and imaginary parts of an imaginary number z=a+bi
        a1= round(-b/(2*a), 2)
        b1= round(math.sqrt(abs(dis))/(2*a), 2)
        b2= round(-math.sqrt(abs(dis))/(2*a), 2)
        #printing the imaginary roots in the correct form
        return(print("z1= {0}+{1}i, z2={0}+{2}i".format(a1,b1,b2)))


main()