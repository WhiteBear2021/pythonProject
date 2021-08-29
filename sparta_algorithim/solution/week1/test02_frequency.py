# ord('알파벳') :아스키코드값 구하는 법, .isalpha()
input = "hello my name is sparta"
alphabet_occurence_array=[0]*26

def find_max_occurred_alphabet(string):
    for char in string:
        if not char.isalpha():
            continue
        num=ord(char)-ord("a")
        alphabet_occurence_array[num]+=1

    return alphabet_occurence_array


result = find_max_occurred_alphabet(input)
print(result)