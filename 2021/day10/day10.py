
#opens the input file as a list strings
with open ("puzzle10") as file:
    puzzle=[line.strip() for line in file]

p = []
for j in puzzle:
    p.append([i.split() for i in j])

# Creating a stack
def create_stack():
    stack = []
    return stack

# Check if stack is empty
def check_empty(stack):
    return len(stack) == 0

# Adding items into the stack
def push(stack, item):
    stack.append(item)

# Removing an element from the stack
def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"
    return stack.pop ()

p1 = []
for k in p:
    top = -1
    stack = create_stack()
    for j in k:
        for i in j:
            if i == '(' or i == '[' or i == '{' or i == '<':
                push (stack, i)
                top += 1
            elif  i == ')' and stack[top] == '(' or i == ']' and stack[top] == '[' or i == '}' and stack[top] == '{' or i == '>' and stack[top] == '<' :    
                pop (stack)
                top -= 1  
            elif i == ')' and stack[top] != '(' or i == ']' and stack[top] != '[' or i == '}' and stack[top] != '{' or i == '>' and stack[top] != '<' :
                push (stack, i)
                top += 1
                break
        else: continue
        break
    p1.append (stack)

p2 = []
p3 = []
for k in p1:
    if k[-1] == ')':
        p2.append (3)
    elif k[-1] == ']':
        p2.append (57)
    elif k[-1] == '}':
        p2.append (1197)
    elif k[-1] == '>':
        p2.append (25137)
    else: p3.append(list(reversed(k)))
        
print ("Part 1 solution:" , sum(p2))

###                part 2

res = []
for i in p3:
    score = 0
    for j in i:
        score = score * 5
        if j == '(':
            score += 1
        elif j == '[':
            score += 2
        elif j == '{':
            score += 3
        elif j == '<':
            score += 4

    res.append (score)

import numpy as np      
print ("Part 2 solution:" , np.median(res))

