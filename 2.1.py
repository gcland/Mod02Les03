submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

submitted.sort(reverse=False)
attended.sort(reverse=False)

submitted_set = set(submitted)
attended_set = set(attended)

if submitted_set & attended_set:
    print("The common element between the submitted list and the attended list is:", submitted_set & attended_set)

else:
    print("No common elements in the two lists.")