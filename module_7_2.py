import io

def custom_write(file_name, strings):
    number_str = 1
    strings_positions = {}
    file = open(file_name, 'a', encoding='utf-8')
    for i in strings:
        strings_positions.update({(number_str, file.tell()): str(i)})
        file.write(str(i))
        file.write('\n')
        number_str += 1
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)