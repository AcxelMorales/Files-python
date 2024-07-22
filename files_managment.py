from ManagmentFile import ManagementFiles

try:
    file = open('test.txt', 'w', encoding='utf-8')
    file.write('Hello World in Python\n')
except Exception as e:
    print(f'Error upload: {e}')
finally:
    file.close()
    print('End to file')

try:
    file = open('test.txt', 'r', encoding='utf-8')
    file2 = open('test.txt', 'a', encoding='utf-8')
    file2.write('Hello in the world jaja')

    print(f'Archivo 1: {file.read()}')

except Exception as e:
    print(f'Error read file: {e}')
finally:
    file.close()

with ManagementFiles('test.txt') as file:
    print(file.read())
