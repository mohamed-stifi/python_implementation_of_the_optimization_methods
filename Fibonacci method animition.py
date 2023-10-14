import math
import time
import numpy as np
import matplotlib.pyplot as plt
###################################################################
def f(x):
    return x*(x-1.5)
def fib(n):
    f0 = 1
    f1 = 1
    f =0
    for i in range(2, n+1):
        f = f0 + f1
        f0 = f1
        f1 = f
    return f1
###################################################################
def Fibonacci(f, x_l, x_u, n):
    """
    parameter :
            x_l = lower bound
            x_u = Upper bound
            n = 
            f = Objective Function
    return :
            x_l = Lower bound given by Fibonacci method
            x_u = Upper bound given by Fibonacci method
            l = long of the interval of uncertainty before Termination
    """
    #----------------------------------
    X = np.linspace(0, 1.1, 100)
    Y = f(X)
    plt.plot(X,Y)
    plt.xlabel('x')
    plt.ylabel('$f(x) = x(x-1.5)$')
    #---------------------------------
    t = 0.1
    plt.ylim(-0.7,0.3)
    plt.xlim(0,1.1)
    plt.title("Fibonacci Search Method")
    xv, y = [], []
    ##-----------------
    ##-----------------
    xv.append(x_l)
    y.append(f(x_l))
    plt.plot(xv, y, c ='y')
    plt.scatter(xv, y, c ='y')
    plt.pause(t)
    ##-----------------
    xv.append(x_u)
    y.append(f(x_u))
    plt.plot(xv, y, c ='y')
    plt.scatter(xv, y, c ='y')
    plt.pause(t)
    ##-----------------
    l = x_u - x_l
    x1 = x_l + (fib(n-2)/ fib(n))*l
    x2 = x_l + (fib(n-1)/ fib(n))*l
    while n>1 :
        plt.clf()
        #----------------------------------
        plt.plot(X,Y, label = '$f(x) = x(x-1.5)$')
        plt.title("Fibonacci Search Method")
        plt.xlabel('x')
        plt.ylabel('$f(x) = x(x-1.5)$')
        #---------------------------------
        plt.ylim(-0.7,0.3)
        plt.xlim(0,1.1)
        #---------------------------------
        n = n - 1
        f1 = f(x1)
        f2 = f(x2)
        if f1 < f2 :
            x_u = x2
            l = x_u - x_l
            x2 = x1
            x1 = x_l + (fib(n-2)/ fib(n))*l
            f2 = f1
            f1 = f(x1)
        elif f1 > f2 :
            x_l = x1
            l = x_u - x_l
            x1 = x2
            f1 = f2
            x2 = x_l + (fib(n-1)/ fib(n))*l
            f2 = f(x2)
        ##-----------------
        xv, y = [], []
        xv.append(x_l)
        y.append(f(x_l))
        xv.append(x_u)
        y.append(f(x_u))
        plt.plot(xv, y, c ='y')
        plt.scatter(xv, y, c ='y')
        plt.pause(t)
        ##-----------------
    plt.show()
    return x_l , x_u , l

###################################################################

Fibonacci(f, 0.0, 1.0, 50)