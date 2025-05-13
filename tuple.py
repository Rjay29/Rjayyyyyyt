my_tuple = (1, 2, 3)
your_tuple = ('a', 'b', 'c')
x, y, z = my_tuple
print(x)
print(y)
print(z)

repeated_tuple = my_tuple * 4
print(repeated_tuple)

print(6 in my_tuple)
print(1 in my_tuple)

plus_tuple = my_tuple + your_tuple
print(plus_tuple)

my_list = list(my_tuple)
print(my_list)

my_list[0] = 'tupal'
print(my_list)

my_set = {3, 6, 9}
my_set.add(12)
print(my_set)

my_set.update([21, 67, 89])
print(my_set)

# list = []
# tuple = ()
# set = {}

set1 = {9, 18, 27}
set2 = {4, 5, 18}
union_set = set1.union(set2)
print(f"1-union: {union_set}")
intersection_set = set1.intersection(set2)
print(f"2-intersection: {intersection_set}")
difference_set = set1.difference(set2)
print(f"3-difference: {difference_set}")
symdiff_set = set1.symmetric_difference(set2)
print(f"4-symdiff: {symdiff_set}")

dic = {"abc": "efg", "123": "456"}
print(len(dic), "px")
