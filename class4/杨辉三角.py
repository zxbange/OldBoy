# def triangles():
#     list  = [1]
#     while True:
#         yield list
#         l = len(list)
#         list = [1]+[list[x]+list[x+1] for x in range(l-1)]+[1]


def triangles():
    l = [1]
    while True:
        yield l
        l.append(0)
        l = [l[i - 1] + l[i] for i in range(len(l))]

a = triangles()
print(next(a))
print(next(a))
print(next(a))
print(next(a))

b = (x for x in range(10))
print(list(b))