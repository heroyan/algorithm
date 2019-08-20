#coding:utf8

'''回溯算法
八皇后问题
'''
import numpy

class EightQueen:
    def __init__(self):
        '''rect 下标表示存储的行号，值表示放在的列号
        '''
        self.queens = 8
        self.rect = numpy.zeros([8], dtype = numpy.int)

    def candrop(self, row, column):
        '''判断第row行，第column列是否能放
        从第一行开始往下放，主要看三个方向是否有冲突（正上方，左上方，右上方）
        '''
        leftUp = column - 1
        rightUp = column + 1
        for i in xrange(row - 1, -1, -1):
            if self.rect[i] == column:
                return False

            if leftUp >=0 and self.rect[i] == leftUp:
                return False

            if rightUp < self.queens and self.rect[i] == rightUp:
                return False

            leftUp -= 1
            rightUp += 1

        return True

    def calQueen(self, row):
        '''从上往下遍历行
        '''
        if row == self.queens:
            # 完成了所有行的遍历
            self.printQueens()
            return

        for i in xrange(0, self.queens):
            # 每行有8个选择
            if self.candrop(row, i):
                self.rect[row] = i
                self.calQueen(row + 1)

    def printQueens(self):
        for i in xrange(0, self.queens):
            tmp = []
            for j in xrange(0, self.queens):
                if self.rect[i] == j:
                    tmp.append('Q')
                else:
                    tmp.append('*')

            print ''.join(tmp)

        print '=============================='

    def run(self):
        self.calQueen(0)

if '__main__' == __name__:
    eq = EightQueen()
    eq.run()