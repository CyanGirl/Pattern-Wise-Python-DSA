'''
Given a string num that contains only digits and an integer target, 
return all possibilities to insert the binary operators '+', '-', and/or '*' between 
the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.
'''

# Two Backtrackings

class Solution:
    def addOperators(self, num: str, target: int):
        ans =[]

        def splitNum(splits,idx):
            if idx>len(num)-1: 
                if len(splits)>0: addOp(splits[0],1,splits[:])
                return

            for i in range(idx,len(num)): 
                splitNum(splits+[num[idx:i+1]], i+1)
                if num[idx]=="0": return

        def addOp(cursum,idx,arr): # generate possible operators additions

            if idx>len(arr)-1: 
                if eval(cursum)==target: ans.append(cursum[:])
                return

            for op in ["+","-","*"]:
                addOp(cursum+op+str(arr[idx]),idx+1,arr)

        splitNum([],0) # generate all possible combinations of numbers
        return ans
    
obj = Solution()
print(obj.addOperators("123",6))