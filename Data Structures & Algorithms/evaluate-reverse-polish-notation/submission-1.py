class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if tokens[i]=="+":
                a=int(stack[-1])+int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(a)
            elif tokens[i]=="-":
                b=int(stack[-2])-int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(b)
            elif tokens[i]=="*":
                c=int(stack[-1])*int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(c)
            elif tokens[i]=="/":
                d=int(stack[-2])/int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(d)
            else:
                stack.append(tokens[i]) 

        return int(stack[0])               
                
        