# create matrix translation and transformation
import math
import numpy as np


def translation_matrix(x:float=1, y:float=1, angule:int=0)->np.array:
    rotation = np.array([np.cos(angule), -np.sin(angule)], )
    
    ...
if __name__ == "__main__":
    a = translation_matrix(1, 0.25)
    b = [[0.5], [0.5], [1.0]]
    t_ab = np.dot(a,b)
    print(t_ab)     






