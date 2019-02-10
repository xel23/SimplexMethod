
class SimplexMethod:
    def __init__(self):
        super().__init__()
        self.smt()

    def methodGaussJordan(self, sTable, l):
        m = len(sTable)
        n = len(sTable[0])
        r = 0

        if sTable[0][l] != 0:
            min = sTable[0][n - 1] / sTable[0][l]
        else:
            min = 1000000000
        for i in range(0, m):
            if sTable[i][l] != 0:
                if sTable[i][n-1] / sTable[i][l] < min:
                    min = sTable[r][n - 1] / sTable[i][l]
                    r = i
            else:
                continue

        for i in range(0, m):
            divider = sTable[i][l] / sTable[r][l]
            if i == r:
                for j in range(0, n):
                    sTable[i][j] /= sTable[r][l]
                continue
            for j in range(0, n):
                sTable[i][j] = sTable[i][j] - sTable[r][j] * divider

        print(sTable)


    def smt(self):
        table = [[2, 3, 1, 2, 1, 1, 0, 0, 1],
                 [2, 1, -3, 2, 1, 0, 1, 0, 3],
                 [2, 1, 2, 1, 0, 0, 0, 0, 1],
                 [-1, 1, -2, 1, 1, 0, 0, 0, 0]]
        table1 = [[-1, 3, 0, 2, 1, 1, 0, 0, 1],
                  [2, -1, 1, 2, 3, 0, 1, 0, 2],
                  [1, -1, 2, 1, 0, 0, 0, 1, 4],
                  [-1, -3, 2, 1, 4, 0, 0, 0, 0]]
        i = -1
        while i < len(table[0]) - 1:
            i += 1
            if table[len(table) - 1][i] > 0:
                self.methodGaussJordan(table, i)
                i = -1


def main():
    ex = SimplexMethod()

if __name__ == "__main__":
    main()