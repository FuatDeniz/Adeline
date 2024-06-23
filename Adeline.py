import numpy as np


def sumofSeries():# for batch mode
    
    
    input=np.array([])    
    input=np.append(x[i],1)
    for k in range(3):
        input=np.multiply(input,error[i]*(-1)*input)
    
    
    return input
    
def GD():#batch mode
    w_b=np.array([])
    w_b=np.append(w,b)
    result=w_b-((1/3)*sum)
    neww=result[:2]
    newb=result[2]
    return neww,newb

def SGD(i):#pattern mode
    err=d[i]-(w[0]*x[i][0]+w[1]*x[i][1]+b)
    input=np.array([])    
    input=np.append(x[i],1)
    
    w_b=np.array([])
    w_b=np.append(w,b)
    
    result=w_b-(0.5*err*(-1)*input)
    neww=result[:2]
    newb=result[2]
    return neww,newb




n=0.5
b=1.0
w=np.array([1.0,1.0]) 
(x)=np.array([[0.0,0.0],[1.0,0.0],[1.0,1.0]])
d=np.array([1,1,2])






print("block adaptive mode results: ")
for j in range(3):
    error=np.array([])
    for i in range (3):
        error=np.append(error,d[i]-(w[0]*x[i][0]+w[1]*x[i][1]+b))     
    
    sum=0
    for i in range(3):
        k=sumofSeries()
        sum=sum+k
    w,b=GD()
    print("weight={},bias={}".format(w,b))

    
print("///////////////////////////////////////////////////")

    
b=1.0
w=np.array([1.0,1.0])

print("Pattern adaptive mode results: ")
for i in range(3):
    w,b=SGD(i)
    print("weight:{},bias:{}".format(w,b))