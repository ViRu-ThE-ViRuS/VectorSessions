X = [1,2,3,4,5,6,7,8,9,10]
List = []
for i in X:
    foo = []
    for y in X:
        foo.append(i*y)
    List.append(foo)
print (List)
