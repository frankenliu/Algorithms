def binary_search(arr, l, r, x):
    """
    implement of binary search.
    time complexity O(Logn)
    :param arr: sorted array
    :param l: array start position
    :param r: array end position
    :param x: search number
    :return: if find, return the position of arr. or,-1 not find.
    """
    if r >= l:
        mid = l + (int)((r - l) / 2)
        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, r, x)
    else:
        return -1


def test():
    A = [12,14,45,56,67,89]
    x = 14
    print("the result is:" + str(binary_search(A, 0, len(A) - 1, x)))