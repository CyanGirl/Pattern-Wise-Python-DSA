"""
You are given two integers n and k and two integer arrays speed and efficiency both of length n. 
There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.

Choose at most k different engineers out of the n engineers to form a team with the maximum performance.
The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.
Return the maximum performance of this team.
Link: https://leetcode.com/problems/maximum-performance-of-a-team/
"""

from heapq import heappush,heappop

class Solution:
    def maxPerformance(self, n: int, speed, efficiency, k: int) -> int:
        
        engs=sorted(list(zip(speed,efficiency)),key=lambda x:(-x[1],-x[0]))
        team=[]  # min heap of K size
        perform=0
        curspeed=0
        
        for sp,ef in engs:
            heappush(team,sp)
            
            if len(team)>k:
                curspeed-=heappop(team) # eliminating the engineer with lowest speed
            curspeed=sp+curspeed # adding the current speed
             
            perform=max(perform, curspeed*ef) # since efficiency is least at current, (max heap) so multiplying with it
    
        return (perform% (10**9+7))
        

        