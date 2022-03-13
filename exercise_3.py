def binary_search(arr: list[int], x: int) -> int:
    low: int = 0
    high: int = len(arr) - 1
    mid: int = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    array = [4, 5, 7, 11, 12, 15, 15, 21, 40, 45]
    x = 11
    result = binary_search(array, x)

if result != -1:
    print(f"Index : {result}")
else:
    print("Element is not in array")