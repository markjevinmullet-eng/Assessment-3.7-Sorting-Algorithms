def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element (Alphabetical: A to Z)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break
    return arr


def main():
    full_name = "Mark Jevin Radaza Mullet"

    # Create the unsorted array:
    # 1. Convert to uppercase for uniform comparison
    # 2. Exclude spaces and symbols using .isalpha()
    # 3. Discard duplicate letters while preserving initial order
    unsorted_array = []
    for char in full_name.upper():
        if char.isalpha() and char not in unsorted_array:
            unsorted_array.append(char)

    # Create a copy of the unsorted array to sort
    sorted_array = bubble_sort(unsorted_array.copy())

    # Output results
    print("Full Name:", full_name)
    print("Unsorted Array (Unique Letters Only):", unsorted_array)
    print("Sorted Array (Alphabetical A-Z):   ", sorted_array)


if __name__ == "__main__":
    main()