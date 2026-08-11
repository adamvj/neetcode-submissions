class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = 0
        current_nums = []
        for i in tokens:
            if i not in ["+", "-", "*", "/"]:
                current_nums.append(int(i))
                #print("current_nums. no operation happening: ", current_nums)
            elif i == '+':
                if len(current_nums) >=2:
                    num1 = current_nums.pop()
                    num2 = current_nums.pop()
                    current_nums.append(num1+num2)
                    #print("Addition result. Appended addition result: ", current_nums)
            elif i == '-':
                if len(current_nums) >=2:
                    num1 = current_nums.pop()
                    num2 = current_nums.pop()
                    current_nums.append(num2-num1)
                    #print("Subtraction result. Subtracting popped from result: ", current_nums)
            elif i == '*':
                if len(current_nums) >=2:
                    num1 = current_nums.pop()
                    num2 = current_nums.pop()
                    current_nums.append(num1*num2)
                    #print("Multiply result. Multiply result by popped: ", current_nums)
            elif i == '/':
                if len(current_nums) >=2:
                    num1 = current_nums.pop()
                    num2 = current_nums.pop()
                    current_nums.append(int(num2/num1))
                    #print("Divide result. Appended division result: ", current_nums)
        return current_nums[-1]
        
