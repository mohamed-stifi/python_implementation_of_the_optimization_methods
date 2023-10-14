import math
import time
import numpy as np
import matplotlib.pyplot as plt
###################################################################
def f(x):
    return x*(x-1.5)
###################################################################
def search_with_fixe_step(f, x_init = 0 ,step = 0.05):
    """
    parameter :
            x_init = initial value of x
            step = step size (x_i - x_{i-1})
            fun = Objective Function
    return :
            interval of uncertainty before Termination of Unrestrıcted search method with fixed step size
    """
    plt.clf()
    t = 0.01
    plt.ylim(-0.7,0.3)
    plt.xlim(0,1)
    plt.title("search_with_fixe_step")
    xv, y = [], []
    f1 = f(x_init)
    xv.append(x_init)
    y.append(f1)
    plt.scatter(xv, y)
    plt.pause(t)
    f2 = f(x_init+step)
    xv.append(x_init+ step)
    y.append(f2)
    plt.scatter(xv, y, c = 'b')
    plt.pause(t)

    if f2 < f1 :
        x_init = x_init + step
        while True :
            f1 = f2
            f2 = f(x_init+step)
            xv.append(x_init+ step)
            y.append(f2)
            plt.scatter(xv, y)
            plt.pause(t)
            if f2 < f1 :
                x_init = x_init + step
            else :
                plt.scatter((x_init - step, x_init+ step), (f(x_init - step), f(x_init+ step)), c = 'y')
                plt.show()
                return (x_init - step, x_init+ step)
    elif f1 < f2 :
        x_init = x_init - step
        while True :
            f1 = f(x_init)
            f2 = f(x_init-step)
            xv.append(x_init-step)
            y.append(f2)
            plt.scatter(xv, y)
            plt.pause(t)
            if f1 > f2 :
                x_init = x_init - step
            else :
                plt.scatter((x_init - step, x_init+ step), (f(x_init - step), f(x_init+ step)), c = 'y')
                plt.show()
                return ( x_init - step, x_init + step)
    else :
        plt.scatter((x_init - step, x_init+ step), (f(x_init - step), f(x_init+ step)), c = 'y')
        plt.show()
        return (x_init - step,x_init + step)
    
###################################################################
search_with_fixe_step(f, x_init = 0 ,step = 0.05)
