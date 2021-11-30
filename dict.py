import operator
month={'jan':1,'feb':2,'mar':3,'jul':4}

sort=dict(sorted(month.items(),key=operator.itemgetter(0)))
print(sort)

