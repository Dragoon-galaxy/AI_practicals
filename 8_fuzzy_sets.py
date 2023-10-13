# Define two fuzzy sets as dictionaries
fuzzy_set_A = {0: 0.4, 1: 0.5, 2: 0.6, 3: 0.7, 4: 0.3}
fuzzy_set_B = {0: 0.5, 1: 0.6, 2: 0.8, 3: 0.9, 4: 0.7}


# Define a function to perform fuzzy set intersection
def fuzzy_intersection(set_A, set_B):
    result_set = {x: round(min(set_A[x], set_B[x]), 2) for x in set_A if x in set_B}
    return result_set


# Define a function to perform fuzzy set union
def fuzzy_union(set_A, set_B):
    result_set = {x: round(max(set_A.get(x, 0), set_B.get(x, 0)), 2) for x in set_A.keys() | set_B.keys()}
    return result_set


# Define a function to compute the complement of a fuzzy set
def fuzzy_complement(set_A):
    result_set = {x: round(1 - membership, 2) for x, membership in set_A.items()}
    return result_set


# Perform fuzzy set operations
intersection_result = fuzzy_intersection(fuzzy_set_A, fuzzy_set_B)
union_result = fuzzy_union(fuzzy_set_A, fuzzy_set_B)
complement_A = fuzzy_complement(fuzzy_set_A)
complement_B = fuzzy_complement(fuzzy_set_B)

# Print the results
print("Fuzzy Set A:", fuzzy_set_A)
print("Fuzzy Set B:", fuzzy_set_B)
print("Intersection:", intersection_result)
print("Union:", union_result)
print("Complement A:", complement_A)
print("Complement B:", complement_B)
