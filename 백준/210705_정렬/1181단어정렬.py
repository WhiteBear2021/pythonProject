import sys
# 단어 갯수 N
N=int(sys.stdin.readline())
word_arr = list(sys.stdin.readline()[:-1] for i in range(N)) 
# wordarr = list((input()) for  in range(N))
word_arr.sort(key=lambda x:(len(x),x))

# print(word_arr)
for i in range(len(word_arr)):
    if i!=0:
        if word_arr[i]==word_arr[i-1]:
            continue
        else:
            print(word_arr[i])
    else:
        print(word_arr[i])
        

# print(word_arr)