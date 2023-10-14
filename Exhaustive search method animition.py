import math
import time
import numpy as np
import matplotlib.pyplot as plt
###################################################################
def f(x):
    return x*(x-1.5)
###################################################################
def exhaustive_Search(fun, a, b, n):
    """
    parameter :
            a = lower bound
            b = Upper bound
            n = Number of Intermediate Points
            fun = Objective Function
    return :
            x1 = Lower bound given by Exhaustive Search Method
            x2 = Upper bound given by Exhaustive Search Method
            iter_ = Number of Iterations before Termination
    """
    #----------------------------------
    X = np.linspace(0, 1.1, 100)
    Y = f(X)
    plt.plot(X,Y)
    plt.xlabel('x')
    plt.ylabel('$f(x) = x(x-1.5)$')
    #---------------------------------
    t = 0.01
    plt.ylim(-0.7,0.3)
    plt.xlim(0,1.1)
    plt.title("Exhaustive Search Method")
    xv, y = [], []
    ##-----------------
    delta = (b-a)/n
    x1 = a
    x2 = x1 + delta
    x3 = x2 + delta
    fx1 = fun(x1)
    ##-----------------
    xv.append(x1)
    y.append(fx1)
    plt.scatter(xv, y, c ='y')
    plt.pause(t)
    ##-----------------
    fx2 = fun(x2)
    ##-----------------
    xv.append(x2)
    y.append(fx2)
    plt.scatter(xv, y, c ='y')
    plt.pause(t)
    ##-----------------
    fx3 = fun(x3)
    ##-----------------
    xv.append(x3)
    y.append(fx3)
    plt.scatter(xv, y, c ='y')
    plt.pause(t)
    ##-----------------
    iter_ = 0
    while fx1>=fx2 and  fx2>=fx3 :
        plt.clf()
        #----------------------------------
        plt.plot(X,Y, label = '$f(x) = x(x-1.5)$')
        plt.title("Exhaustive Search Method")
        plt.xlabel('x')
        plt.ylabel('$f(x) = x(x-1.5)$')
        #---------------------------------
        plt.ylim(-0.7,0.3)
        plt.xlim(0,1.1)
        xv.pop(0)
        y.pop(0)
        ##-----------------
        x1 = x2
        x2 = x3
        x3 = x3 + delta
        fx1 = fx2
        fx2 = fx3
        fx3 = fun(x3)
        ##-----------------
        xv.append(x3)
        y.append(fx3)
        plt.scatter(xv, y, c ='y')
        plt.pause(t)
        ##-----------------
        iter_ = iter_ + 1 
        plt.legend()
    plt.show()
    return x1, x2, iter_

###################################################################
exhaustive_Search(f, 0.0, 1.0, 20)