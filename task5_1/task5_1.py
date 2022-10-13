# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

from random import sample


def words_list(count: int, alp: str = 'абв'):
    some_list = []
    for i in range(count):
        letters = sample(alp, 3)
        some_list.append(''.join(letters))
    return ' '.join(some_list)

#===========================================
# Неудачная попытка - разобраться как улучшить (" абв")
# def words_list(count: int, alp: str = 'абв'):
#   return ' '.join(''.join(sample(alp, 3)) for _ in range(count))

# def chars_replace(words: str) -> str:
#     return words.replace(' абв', '')
# ==========================================

def chars_replace(words: str) -> str:
    input_list = []
    res_list = []
    str_1 = 'абв'
    input_list = words.split()
    for word in input_list:
        if str_1 not in word:
            res_list.append(word)
    return ' '.join(res_list)


new_list = words_list(int(input('Укажите количество слов: ')))
print(new_list)
print(chars_replace(new_list))
