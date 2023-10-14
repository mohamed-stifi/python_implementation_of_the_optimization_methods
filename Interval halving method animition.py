import math
import time
import numpy as np
import matplotlib.pyplot as plt
###################################################################
def f(x):
    return x*(x-1.5)
###################################################################
def interval_Halving(f,x_l, x_u, eps = 1e-4, max_iter = 1000):
    """
    parameter :
            x_l = lower bound
            x_u = Upper bound
            eps = final long of the interval of uncertainty
            max_iter = max Number of Iterations
            f = Objective Function
    return :
            x_l = Lower bound given by Dichotomous search method
            x_u = Upper bound given by Dichotomous search method
            iter_ = Number of Iterations before Termination
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
    plt.title("Interval halving Search Method")
    xv, y = [], []
    ##-----------------
    xv.append(x_l)
    y.append(f(x_l))
    plt.plot(xv, y, c ='y')
    #plt.scatter(xv, y, c ='y')
    plt.pause(t)
    ##-----------------
    xv.append(x_u)
    y.append(f(x_u))
    plt.plot(xv, y, c ='y')
    #plt.scatter(xv, y, c ='y')
    plt.pause(t)
    ##-----------------
    iter_ = 0
    l = x_u - x_l
    while l > eps and iter_ < max_iter :
        plt.clf()
        #----------------------------------
        plt.plot(X,Y, label = '$f(x) = x(x-1.5)$')
        plt.title("Interval halving Search Method")
        plt.xlabel('x')
        plt.ylabel('$f(x) = x(x-1.5)$')
        #---------------------------------
        plt.ylim(-0.7,0.3)
        plt.xlim(0,1.1)
        #--------------------------------------
        l = x_u - x_l
        x0 = (x_u + x_l)/2
        x1 = x0 - l/4
        x2 = x0 + l/4
        fx0 = f(x0)
        fx1 = f(x1)
        fx2 = f(x2)
        if fx1 <fx0 < fx2 :
            x_u = x0
            ##-----------------
            xv.append(x0)
            y.append(fx0)
            plt.plot(xv, y, c ='y')
            #plt.scatter(xv, y, c ='y')
            plt.pause(t)
            ##-----------------
        elif fx1 > fx0> fx2 :
            x_l = x0
            ##-----------------
            xv.append(x0)
            y.append(fx0)
            plt.plot(xv, y, c ='y')
            #plt.scatter(xv, y, c ='y')
            plt.pause(t)
            ##-----------------
        elif fx0 < fx1 and fx0 < fx2 :
            x_u = x2
            x_l = x1
            ##-----------------
            xv.append(x1)
            y.append(fx1)
            xv.append(x2)
            y.append(fx2)
            plt.plot(xv, y, c ='y')
            #plt.scatter(xv, y, c ='y')
            plt.pause(t)
            ##-----------------
        iter_ = iter_ + 1
    plt.show()
    return x_l, x_u, iter_, l

###################################################################
interval_Halving(f,0.0, 1.1 , eps = 1e-9, max_iter = 100)

