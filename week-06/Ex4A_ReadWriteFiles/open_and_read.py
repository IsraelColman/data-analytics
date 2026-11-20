# Israel Colman
# 11/19/2026

with open('about_me.txt', 'r') as f:
    #print(f.read(50))
    #print(f.read(50)) # I get all of the txt file as a list
    #print(f.readline(10))
    #print(f.readline())
    #for i in range(1, 5):
        #print(f.readline())
    #print(f.readlines(1)) # I got the first line as a list
    #print(f.readlines(1)) # I got the first 2 lines as a list
    #print(f.readlines(10)) # I got the first 3 lines as a list
    #print(f.readlines(10)) # I got the first 2 lines as a list again
    #print(f.readlines(100)) # I got the first 3 lines as a list however this time they are on the same line.
    #print(f.readlines(-1)) # I got all of the lines but not its not formated as line by line.
    first_50 = f.read(50)

    next_four_lines = []
    for i in range(4):
        next_four_lines.append(f.readline())
        next_100 = f.readlines(100)

    print(first_50)
    print(next_four_lines)
    print(next_100)

    f.close()