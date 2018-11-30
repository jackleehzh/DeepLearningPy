# coding: utf-8
import numpy as np

def AND(x1, x2):
    b = -3
    electric = np.array([x1, x2])
    ws = np.array([2, 2])
    result = np.sum(electric * ws) + b
    if result <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    b = -3
    electric = np.array([x1, x2])
    ws = np.array([2, 2])
    result = np.sum(electric * ws) + b
    if result <= -3:
        return 0
    else:
        return 1

def NAND(x1, x2):
    b = -3
    electric = np.array([x1, x2])
    ws = np.array([2, 2])
    result = np.sum(electric * ws) + b
    if result <= 0:
        return 1
    else:
        return 0

def OX(x1, x2):
    return AND(OR(x1, x2), NAND(x1, x2))

if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        
        print("AND:" + str(xs) + " -> " + str(AND(xs[0], xs[1])))
        print("OR:" + str(xs) + " -> " + str(OR(xs[0], xs[1])))
        print("NAND:" + str(xs) + " -> " + str(NAND(xs[0], xs[1])))
        print("OX:" + str(xs) + " -> " + str(OX(xs[0], xs[1])))
