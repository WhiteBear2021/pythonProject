def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    for s in newid:
        if s.isalnum() or s in ['-','','.']:
            answer += s
    print(answer)
    while '..' in answer:
        answer = answer.replace('..', '.')
    if answer.startswith('.'):
        answer = answer[1:]
    if answer.endswith('.'):
        answer = answer[:-1]
    if len(answer)==0:
        answer = 'a'
    if len(answer)>=16:
        answer = answer[:15]
        if answer.endswith('.'):
            answer = answer[:-1]
    if len(answer)<=2:
        answer += answer[-1]*(3-len(answer))
    return answer

print(solution("=.="))
print(solution("abcdefghijklmn.p"))