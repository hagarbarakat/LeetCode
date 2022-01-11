class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            "+": lambda a, b: a + b, 
            "-": lambda a, b: a - b, 
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        for i in range(len(tokens)): 
            if tokens[i].lstrip('-').isnumeric(): 
                stack.append(int(tokens[i]))
            else: 
                first = stack.pop()
                second = stack.pop()
                operation = operations[tokens[i]]
                stack.append(int(operation(second, first)))
        return stack[-1]

# ----------------------------------------------------------------------------------------------
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b
        }

        stack = []
        for token in tokens:
            if token in operations:
                number_2 = stack.pop()
                number_1 = stack.pop()
                operation = operations[token]
                stack.append(operation(number_1, number_2))
            else:
                stack.append(int(token))
        return stack.pop()