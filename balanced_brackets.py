#!/bin/python3

# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING brackets as parameter.
def isBalanced(brackets):
    stack = []

    for i in brackets:
        if i == "[":
            stack.append(i)
        elif i == "{" :
            stack.append(i)
        elif i == "(" :
            stack.append(i)

        elif i == ")":
            if stack != [] and stack[-1] == "(":
                stack.pop()
            else: return  "NO"

        elif i == "}" :
            if stack != [] and stack[-1] == "{":
                stack.pop()
            else: return  "NO"

        elif i == "]" :
            if stack != [] and stack[-1] == "[":
                stack.pop()
            else: return  "NO"
        
    return "YES"


if __name__ == '__main__':

    t = int(input().strip())

    results = []
    for t_itr in range(t):
        brackets = input()

        results.append(isBalanced(brackets))

    print(*results, sep='\n')
