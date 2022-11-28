# The Below functions are subjected to Calculation part in a calculator. Name of The program:Scientific Calculator
import math
import cmath
import matplotlib.pyplot as plt
import numpy as np
# To add two numbers
def add(x, y):
    return x + y


# To subtract two numbers
def sub(x, y):
    return x - y


# To multiply two numbers
def mul(x, y):
    return x * y


# To divide two numbers
def div(x, y):
    return x / y


def fact(n):
    return n * (n - 1)


def sqrt(a):
    return a ** (1 / 2)


def compute_hcf(x, y):
    return x


def compute_lcm(x, y):
    return x


def exponent(x):
    return x


def log(x):
    return x


def log10(x):
    return x


def log2(x):
    return x


def perm(x, y):
    return x | y


def comb(x, y):
    return x & y


def pow(x, y):
    return x


def sin(x):
    return x


def cos(x):
    return x


def tan(x):
    return x


def cot(x):
    return x


def sec(x):
    return x


def cosec(x):
    return x





print("Note: Please check the option carefully before you assign operands to an operation!")
# This is a section to select the operation that we desire
print("Select one from below:")
print("1-Addition(+)")
print("2-Subtraction(-)")
print("3-Multiplication(*)")
print("4-Division(/)")
print("5-Factorial(!)")
print("6-Squareroot(√)")
print("7-HCF(x,y)")
print("8-LCM(x,y)")
print("9-Exponent(x)")
print("10-Logarithmic Function")
print("11-Log with base 10")
print("12-Log with base 2")
print("13-Permutation")
print("14-Combination")
print("15-Power")
print("16-remainder")
print("17-Sine values")
print("18-Cosine values")
print("19-Tan Values")
print("20-Cot Values")
print("21-Secant Values")
print("22-Co-secant Values")
print("23-Binary Operation")
print("24-Hexa Decimal Operation")
print("25-Octal Operation")
print("26-Sin(A+B)")
print("27-Sin(A-B)")
print("28-Cos(A+B)")
print("29-Cos(A-B)")
print("30-Tan(A+B)")
print("31-Tan(A-B)")
print("32-Quadratic Equation(ax**2+bx+c=0)")
print("33-Cubic Polynomial(ax**3+bx**2+cx+d=0)")
print("34-Mensuration(square)")



while True:
    func_list = {"1": "ADDITION", "2": "SUBTRACTION", "3": "MULTIPLICATION", "4": "DIVISION", "5": "Factorial",
                 "6": "Squareroot", "7": "HCF", "8": "LCM", "9": "Exponent", "10": "Logarithmic Function",
                 "11": "Log with base 10", "12": "Log with base 2", "13": "Permutation", "14": "Combination",
                 "15": "Power", "16": "Remainder", "17": "Sine Values", "18": "Cosine Values", "19": "Tan Values",
                 "20": "Cot Values", "21": "Secant Values", "22": "Co-secant Values", "23": "Binary Operation","24":"Hexa Decimal Operation","25":"Octal Operation","26":"Sin(A+B)","27":"Sin(A-B)","28":"Cos(A+B)","29":"Cos(A-B)","30":"Tan(A+B)","31":"Tan(A-B)","32":"Quadratic Equation(ax**2+bx+c=0)","33":"Cubic Polynomial(ax**3+bx*2+cx+d=0)","34":" Mensuration(Square)"}
    option = input("Option Selected:")
    # Make sure that the option is from the above four options
    # Enter the inputs in the number format

    if option == '1':
        print("You have selected", func_list.get("1"))
        a = float(input("Enter the 1st number:"))
        b = float(input("Enter the 2nd number:"))
        print(a, "+", b, '=', add(a, b))
    elif option == '2':
        print("You have selected", func_list.get("2"))
        a = float(input("Enter the 1st number:"))
        b = float(input("Enter the 2nd number:"))
        print(a, "-", b, "=", sub(a, b))
    elif option == '3':
        print("You have selected", func_list.get("3"))
        a = float(input("Enter the 1st number:"))
        b = float(input("Enter the 2nd number:"))
        print(a, "*", b, "=", mul(a, b))
    elif option == '4':
        print("You have selected", func_list.get("4"))
        a = float(input("Enter the 1st number:"))
        b = float(input("Enter the 2nd number:"))
        print(a, "/", b, "=", div(a, b))
    elif option == "5":
        print("You have selected", func_list.get("5"))
        a = int(input("enter the number:"))
        print(a, "!", "=", math.factorial(a))
    elif option == "6":
        print("You have selected", func_list.get("6"))
        a = int(input("enter the number:"))
        print("√", a, "=", math.sqrt(a))
    elif option == "7":
        print("You have selected", func_list.get("7"))
        a = int(input("enter the 1st value"))
        b = int(input("enter the 2nd value"))
        print("HCF of", a, b, "is", math.gcd(a, b))
    elif option == "8":
        print("You have selected", func_list.get("8"))
        a = int(input("enter the 1st value"))
        b = int(input("enter the 2nd value"))
        print("HCF of", a, b, "is", math.lcm(a, b))
    elif option == "9":
        print("You have selected", func_list.get("9"))
        a = int(input("enter the number:"))
        print("Exponent of e To the power of ", a, "=", math.exp(a))
    elif option == "10":
        print("You have selected", func_list.get("10"))
        a = int(input("enter the number:"))
        print("Log of", a, "is", "=", math.log(a))
    elif option == "11":
        print("You have selected", func_list.get("11"))
        a = int(input("enter the number:"))
        print("Log of", a, "with base 10 is", "=", math.log10(a))
    elif option == "12":
        print("You have selected", func_list.get("12"))
        a = int(input("enter the number:"))
        print("Log of", a, "with base 2 is", "=", math.log2(a))
    elif option == "13":
        print("You have selected", func_list.get("12"))
        a = int(input("enter the 1st item number:"))
        b = int(input("enter the 2nd item number"))
        print("Permutation of", a, "and", b, "is", "=", math.perm(a, b))
    elif option == "14":
        print("You have selected", func_list.get("13"))
        a = int(input("enter the 1st item number:"))
        b = int(input("enter the 2nd item number"))
        print("Combination of", a, "and", b, "is", "=", math.comb(a, b))
    elif option == "15":
        print("You have selected", func_list.get("15"))
        a = int(input("enter the Base value:"))
        b = int(input("enter the exponent/radical value:"))
        print(a, "To the power of", b, "is", "=", math.pow(a, b))
    elif option == "16":
        print("You have selected", func_list.get("16"))
        a = float(input("enter the numerator value:"))
        b = float(input("enter the denominator value:"))
        print("Remainder of", a, "and", b, "is", "=", math.fmod(a, b))
    elif option == "17":
        print("You have selected", func_list.get("17"))
        a = float(input("enter the angle:"))
        arad = math.radians(a)
        sinx = math.sin(arad)
        sinx_rounded = round(sinx, 2)
        print("Sin(", a, ")", "=", sinx_rounded)
    elif option == "18":
        print("You have selected", func_list.get("18"))
        a = float(input("enter the angle:"))
        arad = math.radians(a)
        cosx = math.cos(arad)
        cosx_rounded = round(cosx, 2)
        print("Cos(", a, ")", "=", cosx_rounded)
    elif option == "19":
        print("You have selected", func_list.get("19"))
        a = float(input("enter the angle:"))
        arad = math.radians(a)
        tanx = math.tan(arad)
        tanx_rounded = round(tanx, 2)
        print("Tan(", a, ")", "=", tanx_rounded)
    elif option == "20":
        print("You have selected", func_list.get("20"))
        a = float(input("enter the angle:"))
        arad = math.radians(a)
        tanx = math.tan(arad)
        tanx_rounded = round(tanx, 2)
        # Note: Cotx= 1/(Tanx)
        cotx = (1 / tanx_rounded)
        print("Cot(", a, ")", "=", cotx)
    elif option == "21":
        print("You have selected", func_list.get("21"))
        a = float(input("enter the angle:"))
        arad = math.radians(a)
        cosx = math.cos(arad)
        cosx_rounded = round(cosx, 2)
        # Note: Sec(x)=1/(Cos(x))
        sec_x = 1 / (cosx_rounded)
        print("sec(", a, ")", "=", sec_x)
    elif option == "22":
        print("You have selected", func_list.get("22"))
        a = float(input("enter the angle:"))
        arad = math.radians(a)
        sinx = math.sin(arad)
        sinx_rounded = round(sinx, 2)
        # Note: Cosec(x)= 1/sin(x)
        cosec_x = 1 / (sinx_rounded)
        print("Cosec(", a, ")", "=", cosec_x)
    elif option == "23":
        print("You have selected", func_list.get("23"))
        k = int(input("Enter the number:"))
        a = bin(k)
        print("Binary number of",k,"is=",a)
    elif option=="24":
        print("You have selected",func_list.get("24"))
        z= int(input("Enter the Number:"))
        g= hex(z)
        print("Hexa decimal number of",z,"is=",g)
    elif option=="25":
        print("You have selected",func_list.get("25"))
        m=int(input("enter the number:"))
        g=oct(m)
        print("Octal number of",m,"is=",g)
    elif option=="26":
        print("You have selected",func_list.get("26"))
        A=float(input("enter the A value:"))
        B=float(input("enter the B value:"))
        Arad= math.radians(A)
        sinA= math.sin(Arad)
        sinA_rounded= round(sinA,2)
        cosA= math.cos(Arad)
        cosA_rounded= round(cosA,2)
        Brad= math.radians(B)
        sinB= math.sin(Brad)
        sinB_rounded= round(sinB,2)
        cosB= math.cos(Brad)
        cosB_rounded= round(cosB,2)
        sinadd=  sinA_rounded*(cosB_rounded)+cosA_rounded*(sinB_rounded)
        print("SinA=",sinA_rounded)
        print("CosA=",cosA_rounded)
        print("SinB=",sinB_rounded)
        print("CosB=",cosB_rounded)
        print("sin(A+B)","=","SinAxCosB+CosAxSinB","=",sinA_rounded,"x",(cosB_rounded),"+",cosA_rounded,"x",(sinB_rounded),"=",sinadd)
    elif option=="27":
        print("You have selected",func_list.get("27"))
        A=float(input("enter the A value:"))
        B=float(input("enter the B value:"))
        Arad= math.radians(A)
        sinA= math.sin(Arad)
        sinA_rounded= round(sinA,2)
        cosA= math.cos(Arad)
        cosA_rounded= round(cosA,2)
        Brad= math.radians(B)
        sinB= math.sin(Brad)
        sinB_rounded= round(sinB,2)
        cosB= math.cos(Brad)
        cosB_rounded= round(cosB,2)
        sinsub=  sinA_rounded*(cosB_rounded)-cosA_rounded*(sinB_rounded)
        print("SinA=",sinA_rounded)
        print("CosA=",cosA_rounded)
        print("SinB=",sinB_rounded)
        print("CosB=",cosB_rounded)
        print("sin(A-B)","=","SinAxCosB-CosAxSinB","=",sinA_rounded,"x",(cosB_rounded),"-",cosA_rounded,"x",(sinB_rounded),"=",sinsub)
    elif option=="28":
        print("You have selected",func_list.get("28"))
        A=float(input("enter the A value:"))
        B=float(input("enter the B value:"))
        Arad= math.radians(A)
        sinA= math.sin(Arad)
        sinA_rounded= round(sinA,2)
        cosA= math.cos(Arad)
        cosA_rounded= round(cosA,2)
        Brad= math.radians(B)
        sinB= math.sin(Brad)
        sinB_rounded= round(sinB,2)
        cosB= math.cos(Brad)
        cosB_rounded= round(cosB,2)
        cosadd=  cosA_rounded*(cosB_rounded)-sinA_rounded*(sinB_rounded)
        print("SinA=",sinA_rounded)
        print("CosA=",cosA_rounded)
        print("SinB=",sinB_rounded)
        print("CosB=",cosB_rounded)
        print("cos(A+B)","=","CosAxCosB-SinAxSinB","=",cosA_rounded,"x",(cosB_rounded),"-",sinA_rounded,"x",(sinB_rounded),"=",cosadd)
    elif option=="29":
        print("You have selected",func_list.get("29"))
        A=float(input("enter the A value:"))
        B=float(input("enter the B value:"))
        Arad= math.radians(A)
        sinA= math.sin(Arad)
        sinA_rounded= round(sinA,2)
        cosA= math.cos(Arad)
        cosA_rounded= round(cosA,2)
        Brad= math.radians(B)
        sinB= math.sin(Brad)
        sinB_rounded= round(sinB,2)
        cosB= math.cos(Brad)
        cosB_rounded= round(cosB,2)
        cossub=  cosA_rounded*(cosB_rounded)+sinA_rounded*(sinB_rounded)
        print("SinA=",sinA_rounded)
        print("CosA=",cosA_rounded)
        print("SinB=",sinB_rounded)
        print("CosB=",cosB_rounded)
        print("Cos(A-B)","=","CosAxCosB+SinAxSinB","=",cosA_rounded,"x",(cosB_rounded),"+",sinA_rounded,"x",(sinB_rounded),"=",cossub)
    elif option=="30":
        print("You have selected",func_list.get("30"))
        print("Choice of Calculation!!!!")
        print("Choices are as follows")
        print("1) Using sinX and cosX")
        print("2) Using Tanx")
        choice=input("Enter the choice you desire(only number):")
        if choice=="1":
            A=float(input("enter the A value:"))
            B=float(input("enter the B value:"))
            Arad= math.radians(A)
            sinA= math.sin(Arad)
            sinA_rounded= round(sinA,2)
            cosA= math.cos(Arad)
            cosA_rounded= round(cosA,2)
            Brad= math.radians(B)
            sinB= math.sin(Brad)
            sinB_rounded= round(sinB,2)
            cosB= math.cos(Brad)
            cosB_rounded= round(cosB,2)
            sinadd=sinA_rounded*(cosB_rounded)+cosA_rounded*(sinB_rounded)
            print(sinadd)
            cosadd=cosA_rounded*(cosB_rounded)-sinA_rounded*(sinB_rounded)
            print(cosadd)
            tanadd=(sinadd/cosadd)
            print("Tan(A+B)=","Sin(A+B)/Cos(A+B)","\n","=","SinACosB+CosASinB/CosACosB-SinASinB","\n","=","(",sinA_rounded,"x",cosB_rounded,"+",cosA_rounded,"x",sinB_rounded,")","/","(",cosA_rounded,"x",cosB_rounded,"-",sinA_rounded,"x",sinB_rounded,")","\n","=",tanadd)
        elif choice=="2":
            A=float(input("Enter the A value:"))
            B=float(input("Enter the B value:"))
            Arad=math.radians(A)
            tanA=math.tan(Arad)
            tanA_rounded=round(tanA,2)
            print(tanA_rounded)
            Brad=math.radians(B)
            tanB=math.tan(Brad)
            tanB_rounded=round(tanB,2)
            print(tanB_rounded)
            tanadd=(tanA_rounded+tanB_rounded)/(1-(tanA_rounded*tanB_rounded))
            print("Tan(A+B)=","(TanA+TanB)/(1-TanATanB)","\n","=","(",tanA_rounded,"+",tanB_rounded,")","/","(",1,"-",tanA_rounded,"x",tanB_rounded,")","\n","=",tanadd)
        else:
            break
    elif option=="31":
        print("You have selected",func_list.get("30"))
        print("Choice of Calculation!!!!")
        print("Choices are as follows")
        print("1) Using sinX and cosX")
        print("2) Using Tanx")
        choice=input("Enter the choice you desire(only number):")
        if choice=="1":
            A=float(input("enter the A value:"))
            B=float(input("enter the B value:"))
            Arad= math.radians(A)
            sinA= math.sin(Arad)
            sinA_rounded= round(sinA,2)
            cosA= math.cos(Arad)
            cosA_rounded= round(cosA,2)
            Brad= math.radians(B)
            sinB= math.sin(Brad)
            sinB_rounded= round(sinB,2)
            cosB= math.cos(Brad)
            cosB_rounded= round(cosB,2)
            sinsub=sinA_rounded*(cosB_rounded)-cosA_rounded*(sinB_rounded)
            print(sinsub)
            cossub=cosA_rounded*(cosB_rounded)+sinA_rounded*(sinB_rounded)
            print(cossub)
            tansub=(sinsub/cossub)
            print("Tan(A-B)=","Sin(A-B)/Cos(A-B)","\n","=","SinACosB-CosASinB/CosACosB+SinASinB","\n","=","(",sinA_rounded,"x",cosB_rounded,"-",cosA_rounded,"x",sinB_rounded,")","/","(",cosA_rounded,"x",cosB_rounded,"+",sinA_rounded,"x",sinB_rounded,")","\n","=",tansub)
        elif choice=="2":
            A=float(input("Enter the A value:"))
            B=float(input("Enter the B value:"))
            Arad=math.radians(A)
            tanA=math.tan(Arad)
            tanA_rounded=round(tanA,2)
            print(tanA_rounded)
            Brad=math.radians(B)
            tanB=math.tan(Brad)
            tanB_rounded=round(tanB,2)
            print(tanB_rounded)
            tansub=(tanA_rounded-tanB_rounded)/(1+(tanA_rounded*tanB_rounded))
            print("Tan(A-B)=","(TanA-TanB)/(1+TanATanB)","\n","=",tanA_rounded,"-",tanB_rounded,"/","(",1,"+",tanA_rounded,"x",tanB_rounded,")","\n","=",tansub)
        else:
            break
    elif option=="32":
        print("You have selected",func_list.get("32"))
        a=float(input("enter the A value:"))
        b=float(input("enter the B value:"))
        c=float(input("enter the C Value:"))
        d= (b**2)-(4*a*c)
        if d<0:
            print("Given equation has no real roots")
        elif d==0:
            a=((-b+(b**2)-4*a*c)/2*a)
            b=a
            print(f"the given equation has single solution:{b}")
            print("Do you want a graph to the given equation?")
            print("Choices are 1)YES;2)NO")
            Choice=input("Enter the choice as stated here:")
            if Choice=="YES":
                plt.style.use("dark_background")
                x = np.linspace(-10, 10)
                y = a * x ** 2 + b * x + c
                fig, ax = plt.subplots()
                ax.set_title("Quadratic Equations with Python")
                ax.plot(x, y)
                plt.scatter(b,a,s=10,marker='o')
                ax.hlines(y=0, xmin=min(x), xmax=max(x), colors='r', linestyles='--', lw=1)
                plt.grid()
                plt.axvline()
                plt.axhline()
                plt.show()
            else:
                print("Thankyou!!!Process Terminates here!!!!")
        else:
            root1=(-b-cmath.sqrt(d))/(2*a)
            root2=(-b+cmath.sqrt(d))/(2*a)
            c=root1
            d=root2
            print("The roots of given equation",a,"x**2","+",b,"x","+",c,"=","0","is:".format(root1,root2),root1,root2)
            print("Do you want a graph to the given equation?")
            print("Choices are 1)YES;2)NO")
            Choice=input("Enter the choice as stated here:")
            if Choice=="YES":
                plt.style.use("dark_background")
                x = np.linspace(-10, 10)
                y = a * x ** 2 + b * x + c
                fig, ax = plt.subplots()
                ax.set_title("Quadratic Equations with Python")
                ax.plot(x, y)
                plt.scatter(c,d,s=10,marker='o')
                ax.hlines(y=0, xmin=min(x), xmax=max(x), colors='r', linestyles='--', lw=1)
                plt.axhline()
                plt.axvline()
                plt.grid()
                plt.show()
            else:
                print("Thankyou!!!!The process terminates here!!!!")

    elif option=="33":
        print("You have selected",func_list.get("33"))
        a=float(input("Enter A value:"))
        b=float(input("Enter B value:"))
        c=float(input("enter C value:"))
        d=float(input("enter D value:"))
        #ax3 + bx2 + cx + d = x3 – (A + B + C)x2 + (AB + BC +CA)x + A*B*C = 0
        X=(a+b+c)
        Y=(a*b+b*c+c*a)
        Z=(a*b*c)
        print("the roots of given polynomial are:",X,Y,Z)
        print("Do you need a graph?")
        choice=input("Enter your choice(YES/NO)")
        
        if choice=="YES":
        
            plt.scatter(X,Y,Z,marker="o")
            x=np.linspace(-10,10)
            y= a*x**3+b*x**2+c*x+d
            plt.plot(x,y)
            plt.grid()
            plt.axvline()
            plt.axhline()
            plt.hlines(y=0, xmin=min(x), xmax=max(x), colors='r', linestyles='--', lw=1)
            plt.show()
        elif choice=="NO":
            print("Thankyou!!!Problem Terminates here!!!")
        else:
            break

    elif option=="34":
        print("you have selected",func_list.get("34"))
        print("a-Area")
        print("b-perimeter")
        print("c-find the side value using area or perimeter")
        opt=input("select the options that you need to perform with a sqaure:")
        if opt=="a":
            print("You have opted to find area")
            side=float(input("enter the side:"))
            area=side*side
            print("Area of square is:",side,"x",side,"=",area)
        elif opt=="b":
            print("You have opted to find perimeter")
            side=float(input("Enter the side:"))
            perimeter=4*side
            print("Perimeter of square is:","4","x",side,"=",perimeter)
        elif opt=="c":
            print("You have opted to find side by giving area or perimeter")
            print("a-Area")
            print("b-perimeter")
            opted=input("Enter whether by which input you wanna find side:")
            if opted=="a":
                print("you have selected to find the side using area")
                area=float(input("enter the area:"))
                side=math.sqrt(area)
                print("The side of the side with the area",area,"is:",area,"^","1/2","=",side)
            elif opted=="b":
                print("you have selected to find the side using perimeter")
                perimeter=float(input("enter the perimeter:"))
                side=(perimeter/4)
                print("The side of the side with the perimeter",perimeter,"is:",perimeter,"/","4","=",side)
                



    


        
        


                
                   
    else:
        break
        


               
                
            

            
        

    
        




        # We can also ask an user to make sure whether he need another calculation
    next_one = input("Do you need another calculation?(Yes/No):")
    if next_one == "No":
        break

else:
    print("Invalid Input")
