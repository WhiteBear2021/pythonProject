import re
def solution(word, pages):
    answer = 0
    wsize=len(word)
    pagedic={}
    for page in pages:
        page_url=re.findall(r'content="https://([\w\.-]+)',page)
        page_href=re.findall(r'href="https://([\w\.-]+)',page)

        print(page_url)
        print(page_href)

        pagedic[page_url[0]]=[]
        pagedic[page_url[0]].append(page_href)
        
        start=page.find("<body>")
        basic=0
        # print(start)
        # res=page.find(word,start)
        # print(res)
        while True:
            res=page.find(word,start+1)
            if res==-1:break
        else:
            if not page[start-1].isalpha() and not page[start+wsize].isalpha():
                basic+=1
            start+=wsize
        print(basic)
        
    return answer


print(solution("blind",["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))