# print(int("010"))
# arr=[("k","1"),("K","01"),("K","010"),("k","001")]
# arr.sort(key=lambda x:(x[0].lower(),int(x[1])))
# print(arr)
import re
def solution(files):
    answer = []
    files=[re.split("([0-9]+)",file) for file in files]
    print(files)
    files.sort(key=lambda x:(x[0].lower(),int(x[1])))
    answer=["".join(file) for file in files]
    return answer


# 입력: ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# 출력: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))

# 입력: ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
# 출력: ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]