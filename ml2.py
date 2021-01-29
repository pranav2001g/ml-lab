import numpy as np
import matplotlib.pyplot as plt
x= np.array([1,2,3])
y=np.array([1.2,1.9,3.2])

a=x.sum()
b=y.sum()
c=(x*x).sum()
d=(y*y).sum()
e=len(x)

w0=(c*b-a*d)/(c*e-a*a)
w1=(b-(e*w0))/a
slope=w1
intercept=w0

values=[slope*i+ intercept for i in x]
plt.title("Maximum Likelihood Linear Function")
plt.xlabel("Datapoints")
plt.ylabel("Fitted points")
plt.scatter(x,y)
plt.plot(x,values,'r')
plt.show() 

