class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for v in tokens:
            if v not in {'+', '-', '*', '/'}:
                nums.append(int(v))
            else:
                post_num = nums.pop()
                pre_num = nums.pop()
                if v == '+':
                    nums.append(pre_num + post_num)
                elif v == '-':
                    nums.append(pre_num - post_num)
                elif v == '*':
                    nums.append(pre_num * post_num)
                else:
                    nums.append(int(pre_num / post_num))
        return nums[0]
        