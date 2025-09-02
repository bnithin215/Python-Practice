
def unique_repeating_elements(arr):
    repeats = []
    for item in set(arr):
        if arr.count(item) > 1:
            repeats.append(item)
    return repeats

# Example usage
nums = [1, 2, 3, 2, 4, 5, 1, 6, 3, 3]
print("Unique repeating elements:", unique_repeating_elements(nums))
