class DynamicModel:
    nodes = []
    pathCost = []
    pListStartFromA = []

    def initModel(self, dataLines):
        # 首先识别全部的状态--全部的字母
        m = dataLines.__len__() - 1
        zimu = []
        for i in range(0, m):
            zimu.append(chr(ord('A') + i))
        print(zimu)
        # 然后识别每个状态
        for i in range(0, m):
            temps = dataLines[i].split(';')
            print(temps)
            n = temps.__len__()
            v = []
            vv = []
            for j in range(0, n):
                if temps.__len__() > 1:
                    v.append("%c%d" % (zimu[i], j + 1))
                else:
                    v.append(zimu[i])

                # 识别各点之间的距离
                vtemp = temps[j].split()
                print("距离：", vtemp)
                nn = vtemp.__len__()
                vvv = []
                for k in range(0, nn):
                    vvv.append(int(vtemp[k]))
                vv.append(vvv)

            print(v)
            self.nodes.append(v)
            print(vv)
            self.pathCost.append(vv)

        print(self.nodes)
        print(self.pathCost)
        return

    def calculateList(self):
        m = len(self.nodes)
        n = len(self.pathCost)
        print(m, n)

        for i in range(m):
            vList = []
            mm = len(self.nodes[i + 1])
            print("第%d层，共有%d种选择。" % (i, mm))

        return
