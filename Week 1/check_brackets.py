# python3

import sys

class Bracket:
    def __init__(self, bracket_type):
        self.bracket_type = bracket_type
        #self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


def check(text):
    opening_brackets_stack = [0]
    index = []
    flag = 0
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(next)
            index.append(i+1)
        if next == ')' or next == ']' or next == '}':
            p = Bracket(opening_brackets_stack[-1])
            if p.Match(next)==True:
                del opening_brackets_stack[-1]
                del index[-1]
            else:
                flag = i+1
                break
    
    if flag == 0 and len(index)==0:
       return 'Success'
    elif flag != 0 :
       return flag
    elif len(index)!=0 :
       return index[-1]

text = input()
print(check(text))            
    # Printing answer, write your code here
