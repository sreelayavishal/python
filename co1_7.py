l=[1,3,6,4]
l2=[1,3,4]
if len(l)==len(l2):
    print("list are of same length")
else:
    print("list are not in same length")
if sum(l)==sum(l2):
    print("the sum are not equal")
else:
    print("the sum are not equal")
print("value occur in both list are:")
print(set(l).intersection(l2))
