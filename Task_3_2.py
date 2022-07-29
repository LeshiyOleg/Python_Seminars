# Определить позицию второго вхождения строки 
# в списке либо сообщить, что её нет.

list_for_checking = ['oleg', 'ksu', 'matvey', 'olegd', 'oleg']

word_to_find = input('Input a word for searching in the list: ')

def find_word_in_list (word, list_for_search):
    count = 0
    flag = False
    for i in range(len(list_for_search)):
        if list_for_search[i] == word:
            count +=1
            if count == 2:
                flag = True
                break
    if flag == True:
        print(f'The 2nd entry of "{word}" in list {list_for_search} has index [{i}]')
    else:
        print(f'There is not the 2nd entry of "{word}" in list {list_for_search}')

find_word_in_list(word_to_find, list_for_checking)
