'''ímplementation of  a simple calculator'''
def add(x,y):
    return x+y

def mul(x,y):
    return x*y
    
def div(x,y):
    return x//y
def sub(x,y):
    return x-y
    
with open("output.txt",'a') as f:
    x=30;y=10
    f.write("addationof two number is: "+str(add(x,y))+"\n")
    f.write("substraction of two numbers is:"+str(sub(x,y))+"\n")
    f.write("Multiplication of two number is:"+str(mul(x,y))+'\n')
    f.write("division of the two numbers is:"+str(div(x,y))+'\n')
    f.write('\n')