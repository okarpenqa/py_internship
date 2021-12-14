def key_item(item):
    return item[1]


main_list = [[1, 3, 3, 4], [2, 1, 3, 5], [4, 0, 1, 7], [5, 2, 1, 0], [0, 4, 8, 3]]
main_list.sort(key=key_item)
print('1.', main_list)
print('_______________________________________________________________________________________________')
main_dictionary = {}
for element in main_list:
    main_dictionary[element[1]] = element[0:]
    main_dictionary[element[1]].pop(1)
print('2.', main_dictionary)
print('_______________________________________________________________________________________________')
for key, value in main_dictionary.items():
    value.sort(reverse=True)
print('3.', main_dictionary)
print('_______________________________________________________________________________________________')
list_set = set([item for sublist in main_dictionary.values() for item in sublist])
print('4.', list_set)
print('_______________________________________________________________________________________________')
string = ', '.join(map(str, list_set))
print('5.', string)
