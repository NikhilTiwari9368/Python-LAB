
file1 = open('read.txt', 'r')
Lines = file1.readlines()
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))
    #print(len(line))
file1.close()