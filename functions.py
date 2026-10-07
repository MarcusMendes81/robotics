# create matrix translation and transformation

import numpy as np


def se2_xy(dx: float = 1, dy: float = 1):
    res = np.array([[np.cos(0), -np.sin(0), dx], [np.sin(0), np.cos(0), dy], [0, 0, 1]])

    return res


def se2_theta(theta):
    res = np.array(
        [
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1],
        ]
    )


if __name__ == "__main__":
    H_r2 = se2_xy(1, 0.25)
    H_p = se2_xy(0.5, 0.5)
    H_final = H_r2 @ H_p
    print(H_final)

    H_r1 = se2_xy(-1, -0.25)
    H_p = se2_xy(0.5, 0.5)
    H_final = H_r1 @ H_p
    print(H_final)
