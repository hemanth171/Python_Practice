#import random
import re

#a = [random.random() for ii in range(0,10)]
#print a
fh = open('/Users/hemanth/git/ud120-projects/final_project/poi_names.txt', 'r')

count = 0
for names in fh:
    #print names
    if names.startswith('(y)') | names.startswith('(n)'):
        count = count + 1
print count