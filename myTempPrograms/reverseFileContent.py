import openpyxl

with open('file1.txt','r') as rFile:
    content = rFile.readlines()
    with open('file1.txt','w') as wFile:
        for line in reversed(content):
            wFile.write(line)



