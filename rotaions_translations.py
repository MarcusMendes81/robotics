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
    return res


def translation_r1_r2(points):
    print("1) As coordenadas do ponto P em no referencial R1")
    H_r2 = se2_xy(1, 0.25)
    H_final = H_r2 @ points
    print(H_final)


def translation_r2_r1(points):
    H_r1 = se2_xy(1, 0.25)
    inv_H_r1 = np.linalg.inv(H_r1)
    H_final_inv = inv_H_r1 @ points
    print("2) As coordenadas do ponto P em no referencial R2")
    print(H_final_inv)


def tr_r1_r2(theta, points):
    print("3) As coordenadas do ponto P em no referencial R1")
    H_r1 = se2_xy(1, 0.25)
    r2_r = se2_theta(theta)
    tr = H_r1 @ r2_r
    p_tr = tr @ points
    print(p_tr)


def tr_r2_r1(theta, points):
    print("4) As coordenadas do ponto P em no referencial R2")
    H_r1 = se2_xy(1, 0.25)
    r2_r = se2_theta(theta)
    tr = H_r1 @ r2_r
    tr_inv = np.linalg.inv(tr)
    p_tr = tr_inv @ points
    print(p_tr)


if __name__ == "__main__":
    radian_45 = np.pi / 4
    tr_r1_r2(radian_45, np.array([[0.5], [0.5], [1.0]]))
    tr_r2_r1(radian_45, np.array([[0.5], [0.5], [1.0]]))
