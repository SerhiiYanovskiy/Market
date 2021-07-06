a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}

a.difference_update(b)
print(a)

c = {"apple", "banana", "cherry"}
d = {"google", "microsoft", "apple"}

c.discard("banana")
print(c)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)

x1 = {"apple", "banana", "cherry"}
y1 = {"google", "microsoft", "facebook"}
z1 = x1.isdisjoint(y1)
print(z1)

myset = {1, 2, 3}
z = myset.issubset([1, 2, 3])
z2 = myset.issubset([1, 2, 3, 4])
print(z, z2)

myset = {1, 2, 3}
z = myset.issuperset([1, 2, 3])
z2 = myset.issuperset([1, 2, 3, 4])
print(z, z2)

A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }

print(A.symmetric_difference(B))
print(B.symmetric_difference(A))

A = {'a', 'b', 'c', 'd'}
B = {'c', 'b', 'd', 'e' }

print(A.symmetric_difference_update(B))
print(B.symmetric_difference_update(A))

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)



