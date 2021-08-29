input = 20


def find_prime_list_under_number(number):
    prime_array=[]
    for i in range(2,number+1):
        occurrence = 0
        for n in range(2,i+1):
            if i%n==0:
                occurrence+=1
        if occurrence==1:
            prime_array.append(i)
    return prime_array


result = find_prime_list_under_number(input)
print(result)