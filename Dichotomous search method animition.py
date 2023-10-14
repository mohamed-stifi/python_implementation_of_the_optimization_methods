import math
import time
import numpy as np
import matplotlib.pyplot as plt
###################################################################
def f(x):
    return x*(x-1.5)
###################################################################
def dichotomous_Search(f,x_l, x_u , delta, eps = 1e-4, max_iter = 1000):
    """
    parameter :
            x_l = lower bound
            x_u = Upper bound
            dleta = small positive number
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
    plt.title("Dichotomous Search Method")
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
    iter_ = 0
    l = x_u - x_l
    while l > eps and iter_ < max_iter :
        #print(iter_)
        plt.clf()
        #----------------------------------
        plt.plot(X,Y, label = '$f(x) = x(x-1.5)$')
        plt.title("Dichotomous Search Method")
        plt.xlabel('x')
        plt.ylabel('$f(x) = x(x-1.5)$')
        #---------------------------------
        plt.ylim(-0.7,0.3)
        plt.xlim(0,1.1)
        #-------------
        l = x_u - x_l
        xc = (x_u + x_l)/2
        x1 = xc - delta/2
        x2 = xc + delta/2
        fx1 = f(x1)
        fx2 = f(x2)
        if fx1 < fx2 :
            x_u = x2
            
        elif fx1 > fx2 :
            x_l = x1
            
        else :
            x_u = x2
            x_l = x1
            
        iter_ = iter_ + 1
        ##-----------------
        xv, y = [],[]
        xv.append(x_l)
        y.append(f(x_l))
        xv.append(x_u)
        y.append(f(x_u))
        plt.plot(xv, y, c ='y')
        plt.scatter(xv, y, c ='y')
        plt.pause(t)
        ##-----------------
    plt.show()
    return x_l, x_u, iter_, l

###################################################################

print(dichotomous_Search(f,0.0, 1.0 , 0.01, eps = 1e-9, max_iter = 100))