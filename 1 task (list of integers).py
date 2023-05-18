def shrink_list(arr):
    left = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
    return arr

nums = [4, 0, 5, 0, 3, 0, 0, 5]
print(nums)
result = shrink_list(nums)
print(result)