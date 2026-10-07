# create matrix translation and transformation

import numpy as np


def se2_xy(dx: float = 1, dy: float = 1):
    res = np.array([
        [np.cos(0), -np.sin(0), dx], 
        [np.sin(0), np.cos(0), dy], 
        [0, 0, 1]])

    return res


def se2_theta(theta):
    res = np.array(
        [
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1],
        ]
    )
    return res




if __name__ == "__main__":
    H_r2 = se2_xy(1, 0.25)
    H_p = np.array([[0.5], [0.5],[1.0]])
    H_final = H_r2 @ H_p
    print(H_final)
    print("="*20)
    H_r1 = se2_xy(1, 0.25)
    inv_H_r1 = np.linalg.inv(H_r1)
    H_final_inv = inv_H_r1 @ H_p
    print(H_final_inv)

    print("="*20)
    
