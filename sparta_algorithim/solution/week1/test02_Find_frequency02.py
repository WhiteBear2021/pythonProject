# 아스키코드를 문자로 chr(65)='A' ord('a')=97
input = "hello my name is sparta"
alphabet_occurence_array=[0]*26

def find_max_occurred_alphabet(string):
    for char in string:
        if not char.isalpha():
            continue
        num=ord(char)-ord("a")
        alphabet_occurence_array[num]+=1

    max_occurence=0
    max_alphabet_index=0
    for index in range(len(alphabet_occurence_array)):
        alphabet_occurence=alphabet_occurence_array[index]
        print(index)

        if alphabet_occurence>max_occurence:
            max_alphabet_index=index
            max_occurence=alphabet_occurence_array[index]
        print(max_alphabet_index)
    return chr(max_alphabet_index+ord('a'))

result = find_max_occurred_alphabet(input)
print(result)