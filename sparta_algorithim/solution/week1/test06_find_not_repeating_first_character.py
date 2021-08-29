input = "abadcabae"


def find_not_repeating_character(string):
    alphabet_array=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    alphabet_num_array=[0]*26
    for char in string:
            num=ord(char)-ord('a')
            alphabet_num_array[num]+=1

    alphabet_not_repeating_array=[]

    for index in range(len(alphabet_num_array)):
        if alphabet_num_array[index]==1:
            alphabet_not_repeating_array.append(chr(index+ord('a')))
    print(alphabet_not_repeating_array)
    for char in string:
        if char in alphabet_not_repeating_array:
            return char



result = find_not_repeating_character(input)
print(result)