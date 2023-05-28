"""
Given a wooden stick of length n units. The stick is labelled from 0 to n. For example, a stick of length 6 is labelled as follows:


Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.
You can change the order of the cuts as you wish.

The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick, it will be split into two smaller sticks 
(i.e. the sum of their lengths is the length of the stick before the cut). 
Please refer to the first example for a better explanation.
Return the minimum total cost of the cuts.
Link : https://leetcode.com/problems/minimum-cost-to-cut-a-stick/description/
"""

class Solution:
    def minCost(self, n: int, cuts) -> int:
        
        '''
        - observing very closely, we can always take one cut at a time. 
        - And the entire length of the stick is to be counted
        - so comibining both above, we can take one cut a time and the only thing we need to
        be concerned about is the length of the stick we can cut at the moment
        - So we can start with the entire length first and take the minimum of all cuts possible
        - For each cut , we again take the possible cuts and min of it and so on
        - until we have exhausted all the cuts
        '''

        memo ={}

        def dfs(left,right): #to keep track of the current length of the stick
            if (right-left)<=1: return 0 # there is no way to cut a 1 length stick

            if memo.get((left,right))==None:

                mincost = float('inf')

                for cut in cuts:
                    # considering we can take the cut in give length
                    if left<cut<right:
                        lefthalf = dfs(left,cut) # this will be a new stick which can be cut again
                        righthalf = dfs(cut,right) # since we cut the stick in two halves

                        mincost=min(mincost, lefthalf+righthalf) # this will be the mincost recursively

                memo[(left,right)] = mincost+(right - left) if mincost!=(float('inf')) else 0 
                # right-left is the length of the stick at the moment

            return memo[(left,right)]

        return dfs(0,n)


