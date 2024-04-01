submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

submitted.sort(reverse=False)
attended.sort(reverse=False)

print(submitted)
print(attended)
if submitted == attended:
    print("The lists are identical.")

else:
    print("The lists are not identical.")

print("The lists are identical:", submitted is attended)