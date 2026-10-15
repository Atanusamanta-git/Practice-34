import math
try:
    a=float(input("Enter coificiant number a: "))
    b=float(input("Enter coificiant number b: "))
    c=float(input("Enter coificiant number c: "))

    if a==0:
        if b==0:
            print("invalid equation!")
        else:
            print(f"Liniar equation root = {-c/b:.2f}")
    else:
        decrement=(b**2)-(4*a*c)
        if decrement>0:
            root1=(-b + math.sqrt(decrement))/(2*a)
            root2=(-b - math.sqrt(decrement))/(2*a)
            print(f"root1= {root1:.2f} and root2={root2:.2f}")
        elif decrement == 0:
            root=-b/(2*a)
            print(f"root1 = root2= {root:.2f}")
        else:
            real_part=-b/(2*a)
            imag_part=math.sqrt(-decrement)/(2*a)
            print(f"root1= {real_part:.2f} + {imag_part:.2f}i and root2={real_part:.2f}-{imag_part:.2f}i")
except ValueError:
    print("Please enter valid numberical values.")
    
