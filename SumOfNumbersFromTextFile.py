import re

fhandle = open('/Users/hemanth/Documents/Python_workspace/regex_sum_323309.txt','r')
s = 0
for line in fhandle:
    y = re.findall('[0-9]+',line.strip())
    if len(y) > 0:
        for x in y:
            s = s + int(x)
print s
