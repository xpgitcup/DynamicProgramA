class DynamicModel:
    nodes = []
    pathCost = []
    pListStartFromA = []
    strategyVector = []

    # 问题的关键是如何规划数据文件的表达形式---
    # 处理单一起点
    def initModel(self, dataLines):
        # 首先识别全部的阶段--全部的字母 = 阶段数+1
        m = len(dataLines) + 1
        zimu = []
        for i in range(0, m):
            zimu.append(chr(ord('A') + i))
        print("全部字母：", zimu)

        # 识别节点
        self.nodes.append(['A'])    # 先增加起始节点
        for i in range(len(dataLines)):
            vtemp = dataLines[i].split(";")
            vvtemp = vtemp[0].split()
            nv = len(vvtemp)
            v = []  # 分析每一行的节点
            for j in range(0, nv):
                if nv > 1:
                    v.append("%c%d" % (zimu[i+1], j + 1))
                else:
                    v.append(zimu[i + 1])
            self.nodes.append(v)

        print(self.nodes)
        print(self.pathCost)
        return

    def calculateList(self):
        print("\n动态规划分析：")
        print(self.nodes)
        m = len(self.nodes) - 1
        print("可以划分成%d个阶段。\n" % m)

        # 对阶段进行循环
        for i in range(m):
            print("\n阶段分析：", self.nodes[i], "--->", self.nodes[i+1] )
            print("状态，阶段的起点", self.nodes[i])
            sm = len(self.nodes[i])
            print("%d 阶段，共有%d个状态" % (i, sm))
            # 可选决策是当前状态的，可能的终点
            dm = len(self.nodes[i + 1])
            print("%d 阶段，可选决策：%d" % (i, dm), self.nodes[i + 1])

            ss = []
            for j in range(0, dm):          # 到底哪个循环放在外面？这是关键--这是终点循环--决策循环
                # 对每个状态进行循环
                distance = []
                for k in range(sm):         # 这时状态循环，起点循环
                    # 路径计算
                    d = {}
                    d['i'] = self.nodes[i][k]  # 起点
                    d['j'] = self.nodes[i + 1][j]  # 终点
                    # 计算长度
                    # 这一句是关键了
                    if (i==0):
                        distance.append(self.pathCost[i+1][j][k])
                    else:
                        distance.append(self.strategyVector[i-1][j]['distance'] + self.pathCost[i+1][j][k])

                # 记录决策---这里缺少--寻优
                print("寻优：", distance)
                # 寻优
                opt = min(distance)
                d['distance'] = opt
                ss.append(d)
                print("%d 阶段 %d状态 决策结果：" % (i, j), opt)
            # 阶段循环完成后，添加进决策列表
            self.strategyVector.append(ss)

        return
