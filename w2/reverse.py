reader = open('test.txt','r')
lines = reader.readlines()
for i in range (len(lines)-1,-1,-1):
    print(lines[i])