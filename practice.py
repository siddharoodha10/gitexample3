import time

'''ímplementation of  a simple calculator'''
def Time(fun):
    def inner(x,y):
        start=time.time()
        ans=fun(x,y)
        time.sleep(2)
        end=time.time()
        return str(ans)+' and time taken is:'+str(end-start)
    return inner

@Time
def add(x,y):
    return x+y

@Time
def mul(x,y):
    return x*y
@Time    
def div(x,y):
    return x//y

@Time
def sub(x,y):
    return x-y

@Time
def rem(x,y):
    return x%y
    
with open("output.txt",'a') as f:
    x=30;y=10
    f.write("addation of two number is: "+add(10,20)+"\n")
    f.write("substraction of two numbers is:"+sub(x,y)+"\n")
    f.write("Multiplication of two number is:"+mul(x,y)+'\n')
    f.write("division of the two numbers is:"+div(x,y)+'\n')
    f.write("Remendr of the x and y is:"+rem(x,y)+"\n")
    f.write('\n')
# print("addationof two number is: "+add(10,20))