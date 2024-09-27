from tkinter import*
import math

screen=Tk()

screen.title("calculator")
screen.geometry("384x524")

def click(b):
    global input
    input= input+ str(b)
    output.set(input)

def clear():
    global input
    input=""
    output.set(input)

def sin():
    global input
    result=eval(input)
    result=toRad(result)
    result=math.sin(result)
    input=str(result)
    output.set(result)

def cos():
    global input
    result=eval(input)
    result=toRad(result)
    result=math.cos(result)
    input=str(result)
    output.set(result)

def tan():
    global input
    result=eval(input)
    result=toRad(result)
    result=math.tan(result)
    input=str(result)
    output.set(result)

def squareroot():
    global input
    result=eval(input)
    result=math.sqrt(result)
    input=str(result)
    output.set(result)

def cuberoot():
    global input
    result=eval(input)
    result=math.cbrt(result)
    input=str(result)
    output.set(result)

def pow():
    global input
    result=eval(input)
    result=math.pow(result,2)
    input=str(result)
    output.set(result)

def log():
    global input
    result=eval(input)
    result=math.log(result)
    input=str(result)
    output.set(result)

def expo():
    global input
    result=eval(input)
    result=math.exp(result)
    input=str(result)
    output.set(result)



def back():
    global input
    result=eval(input)
    result = input[:-1]
    input=str(result)
    output.set(result)

    
def toRad(x):
    x*=math.pi/180
    return x

def equals():
    global input
    result=eval(input)
    input=str(result)
    output.set(result)

output=StringVar()

input=""

result=Entry(screen, bg="cadet blue", font=("arial", 20,"bold"), justify=RIGHT, textvariable=output)

result.place(x=0,y=0,height=60, width=320)

#button sizes= 64x77

bsin=Button(screen, text="sin", font=("arial", 16,"bold"), command=lambda:click("sin"))
bsin=Button(screen, text="sin", font=("arial", 16,"bold"), command=sin, bg="grey")
bsin.place(x=0,y=60,height=77,width=64)

bclear=Button(screen, text="C", font=("arial", 16,"bold"), command=lambda:click("C"))
bclear=Button(screen, text="C", font=("arial", 16,"bold"), command=clear, bg= "red")
bclear.place(x=64,y=60,height=77,width=64)

bforwardbracket=Button(screen, text="(", font=("arial", 16,"bold"), command=lambda:click("("), bg= "orange")
bforwardbracket.place(x=128,y=60,height=77,width=64)

bbackwardbracket=Button(screen, text=")", font=("arial", 16,"bold"), command=lambda:click(")"), bg= "orange")
bbackwardbracket.place(x=192, y=60,height=77,width=64)

bdivision=Button(screen, text="/", font=("arial", 16,"bold"), command=lambda:click("/"), bg= "silver")
bdivision.place(x=256,y=60,height=77,width=64)

bcos=Button(screen, text="cos", font=("arial", 16,"bold"),command=lambda:click("cos"), bg="grey")
bcos=Button(screen, text="cos", font=("arial", 16,"bold"), command=cos, bg="grey")
bcos.place(x=0,y=137,height=77,width=64)

b7=Button(screen, text="7", font=("arial", 16,"bold"), command=lambda:click("7"), bg= "violet")
b7.place(x=64,y=137,height=77,width=64)

b8=Button(screen, text="8", font=("arial", 16,"bold"),command=lambda:click("8"), bg= "violet")
b8.place(x=128,y=137,height=77,width=64)

b9=Button(screen, text="9", font=("arial", 16,"bold"), command=lambda:click("9"), bg= "violet")
b9.place(x=192, y=137,height=77,width=64)

bmul=Button(screen, text="*", font=("arial", 16,"bold"), command=lambda:click("*"), bg= "silver")
bmul.place(x=256,y=137,height=77,width=64)


btan=Button(screen, text="tan", font=("arial", 16,"bold"), command=lambda:click("tan"), bg="grey")
btan=Button(screen, text="tan", font=("arial", 16,"bold"), command=tan, bg="grey")
btan.place(x=0,y=214,height=77,width=64)

b4=Button(screen, text="4", font=("arial", 16,"bold"), command=lambda:click("4"), bg= "violet")
b4.place(x=64,y=214,height=77,width=64)

b5=Button(screen, text="5", font=("arial", 16,"bold"), command=lambda:click("5"), bg= "violet")
b5.place(x=128,y=214,height=77,width=64)

b6=Button(screen, text="6", font=("arial", 16,"bold"), command=lambda:click("6"),bg= "violet")
b6.place(x=192, y=214,height=77,width=64)

bsub=Button(screen, text="-", font=("arial", 16,"bold"), command=lambda:click("-"), bg= "silver")
bsub.place(x=256,y=214,height=77,width=64)

bsquareroot=Button(screen, text="√", font=("arial", 16,"bold"), command=lambda:click("√"), bg="grey")
bsquareroot=Button(screen, text="√", font=("arial", 16,"bold"), command=squareroot, bg="grey")
bsquareroot.place(x=0,y=291,height=77,width=64)

b1=Button(screen, text="1", font=("arial", 16,"bold"), command=lambda:click("1"),bg= "violet")
b1.place(x=64,y=291,height=77,width=64)

b2=Button(screen, text="2", font=("arial", 16,"bold"), command=lambda:click("2"), bg= "violet")
b2.place(x=128,y=291,height=77,width=64)

b3=Button(screen, text="3", font=("arial", 16,"bold"), command=lambda:click("3"), bg= "violet")
b3.place(x=192, y=291,height=77,width=64)

badd=Button(screen, text="+", font=("arial", 16,"bold"), command=lambda:click("+"), bg= "silver")
badd.place(x=256,y=291,height=77,width=64)

bsquare=Button(screen, text="Sq", font=("arial", 16,"bold"),command=lambda:click("Sq"), bg="grey")
bsquare=Button(screen, text="Sq", font=("arial", 16,"bold"),command=pow, bg="grey")
bsquare.place(x=0,y=368,height=77,width=64)

blog=Button(screen, text="Lg", font=("arial", 16,"bold"), command=lambda:click("Lg"), bg="grey")
blog=Button(screen, text="Lg", font=("arial", 16,"bold"), command=log, bg="grey")
blog.place(x=64,y=368,height=77,width=64)

bzero=Button(screen, text="0", font=("arial", 16,"bold"), command=lambda:click("0"), bg= "violet")
bzero.place(x=128,y=368,height=77,width=64)

bdot=Button(screen, text=".", font=("arial", 16,"bold"), command=lambda:click("."), bg= "violet")
bdot.place(x=192, y=368,height=77,width=64)

bEq=Button(screen, text="=", font=("arial", 16,"bold"),command=lambda:click("="), bg= "violet")
bEq=Button(screen, text="=", command=equals, bg= "green")
bEq.place(x=256,y=368,height=144,width=64)


bcuberoot=Button(screen, text="3√", font=("arial", 16,"bold"), command=lambda:click("3√"))
bcuberoot=Button(screen, text="3√", font=("arial", 16,"bold"), command= cuberoot, bg="grey")
bcuberoot.place(x=0,y=445,height=77,width=64)

bexponential=Button(screen, text="^", font=("arial", 16,"bold"), command=lambda:click("^"))
bexponential=Button(screen, text="^", font=("arial", 16,"bold"), command= expo, bg="grey")
bexponential.place(x=64,y=445,height=77,width=64)
    
bbackspace=Button(screen, text="<<", font=("arial", 16,"bold"), command=lambda:click("<<"))
bbackspace=Button(screen, text="<<", font=("arial", 16,"bold"), command= back, bg="orange")
bbackspace.place(x=128,y=445,height=77,width=128)


screen.mainloop()



