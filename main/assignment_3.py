import sys

# Question 1: Euler Method
def f(t, y):
    return t - y**2

def euler_method():
    t0 = 0      # initial time
    y0 = 1      
    t_end = 2   # final time 
    n = 10      # number of iterations
    h = (t_end - t0) / n  #step size
    y = y0
    t = t0
    for _ in range(n):
        y += h * f(t, y) #formula
        t += h
    print(f"{y:.16f}")  #print answer w 16 decimals

# Question 2: Runge-Kutta Method
def runge_kutta():
    t0 = 0      # initial time
    y0 = 1       
    t_end = 2   # final time
    n = 10      # of iterations  
    h = (t_end - t0) / n    # step size
    y = y0
    t = t0
    for _ in range(n):
        k1 = h * f(t, y)     # k1 based on initial slope
        k2 = h * f(t + h/2, y + k1/2)    #k2 at midpoint
        k3 = h * f(t + h/2, y + k2/2)    #k3 at midpoint
        k4 = h * f(t + h, y + k3)
        y += (k1 + 2*k2 + 2*k3 + k4) / 6  # weighted sum to update y
        t += h
    print(f"{y:.15f}") 

# Main Execution
if __name__ == "__main__":
    euler_method()
    runge_kutta()