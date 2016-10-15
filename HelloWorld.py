import re

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@(\S+)',x)
print y

a = 'From: Using the : character'
b = re.findall('^F.+:', a)
print b

q = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
w = re.findall('\S+?@\S+',q)
print w

alist = [2,4,5]
bsum = sum(alist)
print bsum