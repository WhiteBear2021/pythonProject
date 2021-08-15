def solution(input):
    input_array=input.split('\n')
    #     M일동안 N번  
    M,N=map(int,input_array[0].split())
    m=M
    n=N
    answer = ''
    answer=answer+str(M)+' '+str(N)+'\n'
    for i in range(1,len(input_array)):
        if input_array[i]=="SHOW":
            if m>=0 and n>0:
                n-=1
                answer=answer+'1\n'
            else:
                answer=answer+'0\n'
        elif input_array[i]=="NEGATIVE":
            answer=answer+'0\n'
        elif input_array[i]=="NEXT":
            m-=1
            n=N
            answer=answer+'-\n'
        elif input_array[i]=="EXIT":
            answer=answer+'BYE\n'
            break
        else:
            answer=answer+'ERROR\n'
    
    return answer