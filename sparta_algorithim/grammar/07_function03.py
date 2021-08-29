def check_gender(pin):
    num=int(pin.split("-")[1][0:1])
    print(num)
    if num%2==1:
        print("남성")
    else:
        print("여성")

check_gender('150101-1012345')
check_gender('150101-2012345')
check_gender('150101-4012345')

