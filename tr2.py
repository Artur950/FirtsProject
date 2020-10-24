List = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
out = []
for i in List:
    if any(c.isalpha() for c in i):
        out.append((i))
print(out)
