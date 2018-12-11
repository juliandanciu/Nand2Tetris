myfile = open('Square/Square.jack', 'rb');


char = myfile.read(1);
print(char)

if char.decode() == '/':
    print('yeaaahhhh')