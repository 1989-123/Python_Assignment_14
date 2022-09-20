"""
Write a Python script to print distinct elements along with 
their frequencies of occurrence in the list.
"""

l1 = [10, 10, 20, 30, 30, 20, 40, 30, 20]
for i in l1:
    if i in l1:
        print(i, l1.count(i), sep=" --- ")
