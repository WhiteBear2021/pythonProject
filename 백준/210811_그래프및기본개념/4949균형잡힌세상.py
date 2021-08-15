import sys
input=sys.stdin.readline

while True:
    sentence=input()
    if sentence==".":
        break
    bracket_num=0
    sq_bracket_num=0
    chk_bracket=True
    for w in sentence:
        if w=="(":
            bracket_num+=1
            chk_bracket=True
        elif w=="[":
            sq_bracket_num+=1
            chk_bracket=False
        if bracket_num>0 and chk_bracket and w==")":
            bracket_num-=1
        if sq_bracket_num>0 and (~chk_bracket) and w=="]":
            sq_bracket_num-=1
    if bracket_num==0 and sq_bracket_num==0:
        print("yes")
    else:
        print("no")

    
# So when I die (the [first] I will see in (heaven) is a score list).
# [ first in ] ( first out ).
# Half Moon tonight (At least it is better than no Moon at all].
# A rope may form )( a trail in a maze.
# Help( I[m being held prisoner in a fortune cookie factory)].
# ([ (([( [ ] ) ( ) (( ))] )) ]).
#  .
# .