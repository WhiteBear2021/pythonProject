def solution(id_list, reports, k):
    answer = []
    name_dict = {}
    report_dict = {}
     
    for report in reports:
        a, b = report.split()
        if name_dict.get(a):
            len1=len(name_dict[a])
            name_dict[a].update([b])
            len2=len(name_dict[a])
            print(len1,len2)
            print(b,report_dict[b])
            if len1==len2:
                continue
            else:
                if report_dict.get(b):
                    report_dict[b]+=1
                else: 
                    report_dict[b]=1
        else:
            name_dict[a]=set([b])
            if report_dict.get(b):
                report_dict[b]+=1
            else: 
                report_dict[b]=1
    print(report_dict)
    print(name_dict)

    for id in id_list:
        cnt=0
        if name_dict.get(id):
            for name in name_dict[id]:
                if report_dict.get(name):
                    if report_dict[name]>=k:
                        cnt+=1
        answer.append(cnt)

    return answer
# print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))