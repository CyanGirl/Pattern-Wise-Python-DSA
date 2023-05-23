'''
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        - both s and p has to be exhuasted together to be TRUE
        - If star, check for all the combinations hence forward for TRUE
        - for preceding char, check from the pattern
        - . and any char can be directly matched. What cant be matched directly is *.
        - so for * we have to pre look it and consider ZERO or MORE chars
        '''

        memo={}

        def check(sidx,pidx):
            if pidx>len(p)-1:
                return sidx==len(s)

            if memo.get((sidx,pidx)) is None:
                flag = False

                if pidx+1<len(p) and p[pidx+1]=="*": # pre look for cases s=aaab and p=c*a*b
                    if check(sidx,pidx+2): 
                        flag = True # skip 1 char for zero chars case

                    if sidx<len(s) and p[pidx]==".": # matches one or more chars
                        flag= flag or check(sidx+1,pidx)
                    elif sidx<len(s) and p[pidx]==s[sidx]: # match one or more chars
                        flag= flag or check(sidx+1,pidx)

                elif p[pidx]==".":
                    if check(sidx+1,pidx+1): flag = True

                elif sidx<len(s) and  p[pidx]==s[sidx]:
                    flag = flag or check(sidx+1,pidx+1)

                memo[(sidx,pidx)]=flag

            return memo[(sidx,pidx)]

        return check(0,0)
    
