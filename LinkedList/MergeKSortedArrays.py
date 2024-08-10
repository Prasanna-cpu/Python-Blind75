def mergeKSortedArray(arrays):
    merged_array = []

    for array in arrays:
        merged_array.extend(array)

    merged_array.sort()

    return merged_array


print(mergeKSortedArray([[1, 3, 5], [2, 4, 6]]))
