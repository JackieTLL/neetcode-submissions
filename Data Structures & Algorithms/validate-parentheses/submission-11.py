class Solution:
    def isValid(self, s: str) -> bool:
        if s == '':
            return True
        parentheses_dict = {')': '(', ']': '[', '}': '{'}
        help_stack = []
        for ch in s:
            if ch in ['(', '[', '{']:
                help_stack.append(ch)
            else:
                if not help_stack:
                    return False
                elif help_stack[-1] == parentheses_dict[ch]:
                    help_stack.pop()
                else:
                    help_stack.append(ch)
        return help_stack == []

        