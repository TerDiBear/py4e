

r = open('text.txt')
r1 = set(r.read().split())
r.close()

r = open('text2.txt')
r2 = set(r.read().split())
r.close()

#new = r1.intersection(r2)
new = r2.difference(r1)

print(new)
