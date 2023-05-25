'''
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, 
LeetCode would like to work on some projects to increase its capital before the IPO. 
Since it has limited resources, it can only finish at most k distinct projects before the IPO. 
Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of 
capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.
Link : https://leetcode.com/problems/ipo/description/
'''

from heapq import heappush, heappop

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits, capital) -> int:
        '''
        - pair of profit and captial
        - captial is needed to do work. So a min heap is needed to filter out doable word wrt to cur w
        - now once we get doable works, we want to do the max of it. so a max heap
        - we run this until k<1 or len(captial)<1
        '''

        paired = []
        # captial to be less so that we can get do-able works within our current capital w
        for i in range(len(profits)):
            heappush(paired, (capital[i],profits[i]))

        curcap = w
        doables=[]

        while k>0: # till we have got all the works

            while paired and paired[0][0]<=curcap: # while capital is afforable
                cap, prof= heappop(paired)
                heappush(doables, -prof) # max heap for profits

            if len(doables)>0: 
                curprofit = -heappop(doables) # do the current work
                curcap+=curprofit
                k-=1
            else: break

        return curcap