from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        opArr = []
        print(operations)
        for op in operations:
            if (op == "+"):
                opArr.append(opArr[-2] + opArr[-1])
            elif (op == 'D'):
                opArr.append(opArr[-1] * 2)
            elif (op == 'C'):
                opArr.pop()
            else:
                opArr.append(int(op))
        return sum(opArr)