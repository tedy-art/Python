"""
WAP to sort (asending and descending ) a dictionary by value.
"""

import operator
d = {}
d[1]=2
d[3]=4
d[4]=3
d[2]=1
d[0]=0
print("Original dictionary : ",d)

sorted_d = sorted(d.items(), key = operator.itemgetter(1))
print("Dictionary in acending order value : ", sorted_d)

sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print("Dictionary in descending order by values : ", sorted_d)