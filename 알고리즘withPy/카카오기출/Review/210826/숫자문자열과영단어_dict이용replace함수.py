# result

# "one4seveneight" -> 1478
# "23four5six7" ->	234567
# "2three45sixseven" ->	234567
# "123"	-> 123

def solution(s):
    answer = ""
    dic={"one":"1","two":"2","three":"3",
         "four":"4","five":"5","six":"6",
         "seven":"7","eight":"8",'nine':'9','zero':"0"}
    val=""
    for str in s:
        if str.isalpha():
            val+=str
            if dic.get(val):
                answer+=dic.get(val)
                val=""
        else:
            val=""
            answer+=str
                
    return int(answer)

print(solution("2three45sixseven"))