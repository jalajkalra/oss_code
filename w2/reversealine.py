reader = open('test.txt','r')
lines = reader.readlines()
for i in range (0,len(lines)):
    print(lines[i][::-1])