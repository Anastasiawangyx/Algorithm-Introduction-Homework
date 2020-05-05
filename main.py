from homework4 import Bellman_Ford, Floyd
import numpy as np


def main():
    '''
    v0 = 1
    G = {
        1: {1: 0, 2: 6, 5: 7},
        2: {2: 0, 3: 5, 4: -4, 5: 8},
        3: {2: -2, 3: 0},
        4: {1: 2, 3: 7, 4: 0},
        5: {3: -3, 4: 9, 5: 0}
    }
    dis = Bellman_Ford(G, v0)
    print(dis.values())
    '''

    INF = 999  # 代表无穷大
    D = np.array([[0, 3, 8, INF, -4],
                  [INF, 0, INF, 1, 7],
                  [INF, 4, 0, INF, INF],
                  [2, INF, -5, 0, INF],
                  [INF, INF, INF, 6, 0]])
    Floyd(D)


if __name__ == "__main__":
    main()
