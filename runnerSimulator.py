#coding:utf8

'''模拟运动员，百米赛跑
要求：全部人跑完再输出结果
'''
from threading import Thread
import time
import random

MAX_TIME_TO_RUN = 12

class Runner(Thread):
    '''运动员
    多线程实现，每个运动员是一个线程
    '''
    def __init__(self, number, name, results = []):
        super(Runner, self).__init__()

        self.number = number
        self.name = name
        self.results = results


    def run(self):
        print 'run', self.number
        
        timeCost = MAX_TIME_TO_RUN*random.random()
        time.sleep(timeCost)
        self.results.append((self.number, self.name, timeCost))


class Race(object):
    '''一场比赛，初始化n个运动员
    '''
    def __init__(self, numOfRunner):
        self.results = []
        self.numOfRunner = numOfRunner
        self.runners = []

        for i in xrange(0, numOfRunner):
            self.runners.append(Runner(i+1, 'name%s' % (i+1), self.results))


    def showResults(self):
        '''打印比赛结果
        '''
        print 'here comes the hero! congratulations!'
        for num, name, timeCost in self.results:
            print num, name, ': %ss' % timeCost


    def run(self):
        '''一声枪响，逃之夭夭！
        '''
        print 'boooooom! begin running...'

        for i in xrange(0, self.numOfRunner):
            self.runners[i].start()

        for i in xrange(0, self.numOfRunner):
            self.runners[i].join()

        self.showResults()


if __name__ == '__main__':
    race = Race(20)
    race.run()