"""
Given a string representing an expression of parentheses containing the characters '(', ')', '[' , ']' , '{' , or '}', determine if the expression forms a valid sequence of parentheses.
A sequence of parentheses is valid if every opening parenthesis has a corresponding closing parenthesis, and no closing parenthesis appears before its matching opening parenthesis.

Example 1:
Input: s = "([]{})"
Output: True

Example 2:
Input s = "([]{)}"
Output
False

Explanation: The ' ( ' parenthesis is closed before its nested ' { ' parenthesis is closed.
"""

def solution(string:str) -> bool:
    string_lenght = len(string)
    stack = list()
    if string_lenght % 2 != 0:
        return False
    for char in string:
        if char in ["(", "[", "{"]:
            stack.append(char)
        elif char == ")":
            if stack[-1] != "(":
                return False
            stack.pop()
        elif char == "]":
            if stack[-1] != "[":
                return False
            stack.pop()
        elif char == "}":
            if stack[-1] != "{":
                return False
            stack.pop()
    return True

print(solution("([]{})"))
print(solution("([]{)}"))

# problems
# print(solution(")")) --> raises IndexError
# print(solution("(")) --> return True


# thsoudu after study
def solution(string:str) -> bool:
    string_lenght = len(string)
    stack = list()
    pairs = {
        "(" : ")",
        "[" : "]",
        "{" : "}",
    }
    if string_lenght % 2 != 0:
        return False
    for char in string:
        if char in pairs:
            stack.append(char)
        else:
            if (not stack) or (pairs[stack[-1]] != char):
                return False
            stack.pop()
    return len(stack) == 0

print(solution("([]{})"))
print(solution("([]{)}"))
print(solution(")")) 
print(solution("("))
