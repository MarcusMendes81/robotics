import numpy as np

def rx(theta):
    return np.array([
    [1.0, 0.0 , 0.0],
    [0.0, np.cos(theta), -np.sin(theta)],
    [0.0, np.sin(theta), np.cos(theta)]
    ])


def ry(theta):
    return np.array([
    [np.cos(theta), 0.0, np.sin(theta)],
    [0.0, 1.0 , 0.0],
    [-np.sin(theta), 0.0 ,np.cos(theta)]
    ])


def rz(theta):
    return np.array([
    [np.cos(theta), -np.sin(theta), 0.0],
    [np.sin(theta), np.cos(theta), 0.0],
    [0.0, 0.0 , 1.0]
    ])


if __name__ == "__main__":
    theta = np.pi/2
    result = rx(theta) @ ry(theta)    
    print(result)
    print("="*15)
    result_2 = ry(theta) @ rx(theta)
    print(result_2)