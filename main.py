# scripts for testing toy problems

# quick sort
def my_quick_sort(arr, descending=False):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    result = my_quick_sort(left) + mid + my_quick_sort(right)
    if descending:
        result = result[::-1]
    return result


testArr = ['A', 'C', 'B', 'E', 'E', 'A', 'F', 'B']
print(my_quick_sort(testArr))
print(my_quick_sort(testArr, descending=True))
testArr.sort()
print(testArr)
testArr.sort(reverse=True)
print(testArr)
testArr = [3, 2, 4, 1, 0, -1, -6, 5, 4, 7, 9]
print(my_quick_sort(testArr))
print(my_quick_sort(testArr, descending=True))
