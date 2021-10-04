def is_available(candidate,current_col):
    current_row=len(candidate)

def DFS(N,current_row,current_candidate,final_result):
    if current_row==N:
        final_result.append(current_candidate)
        return
    else:
        for candidate_col in range(N):
            if is_available(current_candidate,candidate_col):
                current_candidate.append(candidate_col)
                DFS(N,current_row+1,current_candidate,final_result)
                current_candidate.pop()
        
    
def solve_n_queen(N):
    final_result=[]
    DFS(N,0,[],final_result)
    return final_result