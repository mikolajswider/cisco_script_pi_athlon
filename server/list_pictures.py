import os

def list_files(path):
    l=[]
    line=''
    output = os.popen('ls -1 '+ path).read()
    for char in output:
        if char == '\n':
            l.append(line)
            line=''
        else:
            line=line+char
    return l
