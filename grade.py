# Prompt user for input
set1 = set(map(int, input("Enter elements of the first set: ").split()))
set2 = set(map(int, input("Enter elements of the second set: ").split()))

# Compute union and intersection
union_result = set1 | set2
intersection_result = set1 & set2

# Display the results
print("Union:", union_result)
print("Intersection:", intersection_result)
