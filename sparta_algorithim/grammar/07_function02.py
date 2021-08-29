def bus_rate(age):
    if age>65:
        print("무료입니다")
    elif age>20:
        print("성인입니다")
    else:
        print("청소년입니다")

bus_rate(30)
bus_rate(15)

def bus_rate(age):
    if age>65:
        return 0
    elif age>20:
        return 1000
    else:
        return 750

print(bus_rate(30))
print(bus_rate(15))
