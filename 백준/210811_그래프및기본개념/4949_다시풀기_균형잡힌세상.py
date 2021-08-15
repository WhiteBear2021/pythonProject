import sys 
input = sys.stdin.readline 
while 1: 
    string = input().rstrip() 
    stack = [] 
    true_flag = 1 
    for cha in string: 
        if cha == '(' or cha == '[': 
            stack.append(cha) 
        elif cha == ')': 
            if stack and stack[-1] == '(': 
                stack.pop() 
            else: 
                true_flag = 0 
                break 
        elif cha == ']': 
            if stack and stack[-1] == '[': stack.pop() 
        else: 
            true_flag = 0 
            break 
        if string == '.': break 
        print("yes" if true_flag and not(stack) else "no")


    
# So when I die (the [first] I will see in (heaven) is a score list).
# [ first in ] ( first out ).
# Half Moon tonight (At least it is better than no Moon at all].
# A rope may form )( a trail in a maze.
# Help( I[m being held prisoner in a fortune cookie factory)].
# ([ (([( [ ] ) ( ) (( ))] )) ]).
#  .
#  .