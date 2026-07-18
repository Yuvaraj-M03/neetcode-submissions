class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        rea = [0]*len(temperatures)
        stack = []
        for i,a in enumerate(temperatures):
            while stack  and a >stack[-1][0]:
                stackT,stackIn =stack.pop()
                rea[stackIn]= i-stackIn
            stack.append((a,i))
        return rea
        