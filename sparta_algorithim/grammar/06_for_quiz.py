num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
count=0
for num in num_list:
    if num%2==0:
        print(num)
        count+=1
print("짝수 갯수:")
print(count)


sum=0
for num2 in num_list:
    sum+=num2
print(sum)

max=0
for num3 in num_list:
    if max<num3:
        max=num3

print(max)