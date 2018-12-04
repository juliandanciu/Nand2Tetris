f = open('ArrayTest/MainTest.jack')

for i in range(600):

    current_position = f.tell()

    if current_position > 6000:
        print(f.tell())
    f.read(1)

