'''

With using complex math module:

Program to take any real quadratic equation in the form ax**2+bx+c=0 
and return the roots x1 and x2 to 2 decimal places

- Josh McCall
'''

import cmath

def main():
    print("This is a program to give the roots of a quadratic equation of the form: ax^2+bx+c=0 where a,b and c are real")
    #taking input values
    a= float(input("What is the a value?"))
    b= float(input("What is the b value?"))
    c= float(input("What is the c value?"))

    #calculate discriminant
    dis = b**2-4*a*c

    #find solutions
    x1 = (-b+cmath.sqrt(dis))/(2*a)
    x2 = (-b-cmath.sqrt(dis))/(2*a)

    #return cases in concise form
    if a==0:
        return(print("Error: equation is not quadratic if a=0"))
    elif x1==x2:
        return((print("Repeated root: x=", x1)))
    else:
        return((print("x1={0}, x2={1}".format(x1,x2))))
    
main()
