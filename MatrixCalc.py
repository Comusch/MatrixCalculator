import math

class Calc:

    def __init__(self, matrix):
        self.m = matrix
        self.print()

    def __detl__(self, m):
        if len(m) == 1:
            return m[0][0]
        r = 0
        for i in range(len(m)):
            r += m[i][0]*self.__detl__(self.__create_new_Matrix__(m, i, 0)) * (-1)**(i+1)

        return r

    def __create_new_Matrix__(self, m, w_o_i, w_o_j):
        new_m = []
        for i in range(len(m)):
            new_c = []
            if i == w_o_i:
                continue
            for e in range(len(m[i])):
                if e == w_o_j:
                    continue
                new_c.append(m[i][e])

            new_m.append(new_c)

        return new_m

    def getDet(self):
        r = self.__detl__(self.m)
        return r

    def it_has_a_kern(self):
        if self.getDet() != 0:
            return False
        return True

    def Gauß_on(self):
        m = self.m
        for z in range(len(m)):
            for i in range(len(m)-z-1):
                pro = m[z+i+1][z]/m[z][z]*(-1)
                for e in range(len(m)):
                    m[z+i+1][e] += m[z][e]*pro

        self.m = m

    def get_Invertierte_Matrix(self):
        i_m = []
        for i in range(len(self.m)):
            new_c = []
            for e in range(len(self.m)):
                if e ==i:
                    new_c.append(1)
                else
                    new_c.append(0)
            i_m.append(new_c)
        #"douple Gauß"
        return i_m


    def print(self):
        for i in range(len(self.m)):
            print(self.m[i])


