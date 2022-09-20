# Write a Python script to remove all non int values from a list.

l1 = [10, 20, "Jayesh", 40, True, 4.5,"patel", 5.6, 46, 7.8, 100]
l2 = []
for i in l1:
    if type(i) == int:
        l2.append(i)
print()
print(l2)
print()
