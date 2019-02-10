class Task:
    def __init__(self):
        super().__init__()
        self.task = [[1, 2, 40],
                     [3, 2, 30],
                     [1, 4, 30],
                     [30, 70, 100]]
        # self.task = [[1, 2, 4, 90],
        #              [1, 3, 4, 30],
        #              [2, 2, 3, 40],
        #              [50, 60, 10, 120]]
        self.methodMinElement()

    def updater(self, workMatrix):
        for i in range(0, len(workMatrix) - 2):
            for j in range(0, len(workMatrix[0]) - 2):
                if workMatrix[i][j][1] == 0:
                    if workMatrix[i][j][0] > workMatrix[i][j][2]:
                        maxDif = [0, j]
                        for k in range(0, len(workMatrix[0]) - 2):
                            if maxDif[0] < workMatrix[i][k][2]:
                                maxDif = [workMatrix[i][k][2], k]
                        workMatrix[i][j][1] = workMatrix[i][maxDif[1]][1]
                        workMatrix[i][maxDif[1]][1] = 0
                        dif = workMatrix[i][maxDif[1]][2] - workMatrix[i][j][2]
                        minDif = [[0, i]]
                        for k in range(0, len(workMatrix) - 2):
                            if dif > workMatrix[k][maxDif[1]][2] - workMatrix[k][j][2] > minDif[0][0]:
                                minDif.append([workMatrix[k][maxDif[1]][2] - workMatrix[k][j][2], k])
                        minDif.sort()
                        workMatrix[minDif[-1][1]][maxDif[1]][1] += workMatrix[minDif[-1][1]][j][1]
                        workMatrix[minDif[-1][1]][j][1] = 0
        return


    def setPotencial(self, workMatrix, minCost):
        workMatrix[minCost[-1][1]][-2][0] = round(minCost[-1][0] / 2)
        workMatrix[-1][minCost[-1][2]] = workMatrix[minCost[-1][1]][minCost[-1][2]][2] - \
                                                        workMatrix[minCost[-1][1]][-2][0]

        for i in range(minCost[-1][1], len(workMatrix) - 1):
            for j in range(0, len(workMatrix[0]) - 2):
                if workMatrix[i][j][1] != 0:
                    if workMatrix[i][-2][0] != self.empty:
                        workMatrix[-1][j] = workMatrix[i][j][2] - workMatrix[i][-2][0]
                        for k in range(0, len(workMatrix) - 2):
                            workMatrix[k][-2][0] = workMatrix[k][j][2] - workMatrix[-1][j]
                    else:
                        workMatrix[i][-2][0] = workMatrix[-1][j] - workMatrix[i][j][0]

        for i in range(minCost[-1][1], -1, -1):
            for j in range(0, len(workMatrix[0]) - 2):
                if workMatrix[i][j][1] != 0:
                    if workMatrix[i][-2][0] != self.empty:
                        workMatrix[-1][j] = workMatrix[i][j][2] - workMatrix[i][-2][0]
                        for k in range(0, len(workMatrix) - 2):
                            workMatrix[k][-2][0] = workMatrix[k][j][2] - workMatrix[-1][j]
                    else:
                        workMatrix[i][-2][0] = workMatrix[-1][j] - workMatrix[i][j][2]

        for i in range(minCost[-1][1], -1, -1):
            for j in range(0, len(workMatrix[0]) - 2):
                if workMatrix[i][j][1] == 0:
                    workMatrix[i][j][0] = workMatrix[i][-2][0] + workMatrix[-1][j]

        self.updater(workMatrix)


    def methodMinElement(self):
        self.empty = 999999999
        workMatrix = [[[]]]
        minCost = [[]]
        for i in range(0, len(self.task)):
            for j in range(0, len(self.task[0]) + 1):
                workMatrix[i][0] = [self.empty, 0, self.task[i][0]]
                if i < len(self.task) - 1 and j < len(self.task[0]) - 1:
                    minCost.append([self.task[i][j], i, j])
                if j == len(self.task[0]):
                    workMatrix[i].append([])
                    continue
                if j != 0:
                    workMatrix[i].append([self.empty, 0, self.task[i][j]])
            workMatrix.append([self.empty])

        for i in range(0, len(self.task[0]) + 1):
            workMatrix[len(workMatrix) - 1].append(self.empty)
        minCost.pop(0)
        minCost.sort()

        for i in range(0, len(minCost)):
            if workMatrix[minCost[i][1]][-2][2] >= workMatrix[-2][minCost[i][2]][2]:
                workMatrix[minCost[i][1]][minCost[i][2]][1] = workMatrix[-2][minCost[i][2]][2]
                workMatrix[minCost[i][1]][-2][2] -= workMatrix[-2][minCost[i][2]][2]
                workMatrix[-2][minCost[i][2]][2] = 0
            else:
                workMatrix[minCost[i][1]][minCost[i][2]][1] = workMatrix[minCost[i][1]][-2][2]
                workMatrix[-2][minCost[i][2]][2] -= workMatrix[minCost[i][1]][-2][2]
                workMatrix[minCost[i][1]][-2][2] = 0

        self.setPotencial(workMatrix, minCost)

        return

def main():
    t = Task()

if __name__ == "__main__":
    main()