# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

from itertools import groupby, starmap
from os import path


def rle_encode(text='input_text', code_text='encoded_text.txt'):
    if path.exists(text) and not path.exists(code_text):
        with open(text) as my_f_1, \
                open(code_text, 'a') as my_f_2:
            for i in my_f_1:
                my_f_2.write(
                    ''.join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
    else:
        print('Файл не найден!')


def rle_decode(name):
    if path.exists(name):
        with open(name) as my_f:
            n = ''
            for k in my_f:
                word_nums = []
                for i in k.strip():
                    if i.isdigit():
                        n += i
                    else:
                        word_nums.append([int(n), i])
                        n = ''
                print(''.join(starmap(lambda x, y: x * y, word_nums)))
    else:
        print('Файл не найден!')


# def rle_decode(name):
#     if path.exists(name):
#        with open(name) as my_f:
#            for i in my_f:
#                 word_nums = [''.join(g) for k, g in groupby(i.strip(), key=str.isdigit)]
#                 print(''.join([f'{int(word_nums[i]) * word_nums[i+1]}' for i in range(0, len(word_nums), 2)]))
#     else:
#        print("Файл не найден!")
#

rle_encode('input_text.txt')
rle_decode('encoded_text.txt')

# =======================================================

# def encode_rle(txt):
#     enigma = ""
#     i = 0
#     while i < len(txt):
#         count = 1
#         while i + 1 < len(txt) and txt[i] == txt[i + 1]:
#             count += 1
#             i += 1
#         enigma += str(count) + txt[i]
#         i += 1
#     return enigma


# def decode_rle(data):
#     decoding = ""
#     count = ""
#     for char in data:
#         if char.isdigit():
#             count += char
#         else:
#             decoding += char * int(count)
#             count = ""
#     return decoding


# def read_data(file):
#     with open(str(file), "r", encoding="utf-8") as data:
#         input_string = data.read()
#     return input_string


# input_text = "input_text.txt"                             # исходный текст
# tx = 'encoded_input_text.txt'                             # сжатый текст
# text1 = "decoded_text.txt"                                # восстановленный текст
# print(read_data(input_text))                              # исходный текст
# print(encode_rle(read_data(input_text)))                  # сжатый текст
# with open(str(tx), "w", encoding="utf-8") as data:
#     data.write(encode_rle(read_data(input_text)))
# print(decode_rle(read_data(tx)))                          # восстановленный текст
# with open(str(text1), "w", encoding="utf-8") as data:
#     data.write(decode_rle(read_data(tx)))
