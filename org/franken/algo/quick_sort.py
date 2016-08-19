def partition(arr, low, high):
    """
    This function takes the first element as pivot.
    places the pivot element at its correct position
    in sorted array, and places all smaller (smaller than pivot)
    to left of pivot and all greater elements to right of pivot
    :param arr: unsort array
    :param low: the start position of arr
    :param high: the end position of arr
    :return: the pivot position
    """
    pivot = arr[low]
    while low < high:
        while low < high and arr[high] > pivot:
            high -= 1
        arr[low], arr[high] = arr[high], arr[low]
        while low < high and arr[low] < pivot:
            low += 1
        arr[low], arr[high] = arr[high], arr[low]
    return low


def partition2(arr, low, high):
    """
    This function takes last element as pivot, places
    the pivot element at its correct position in sorted
    array, and places all smaller (smaller than pivot)
    to left of pivot and all greater elements to right
    of pivot
    :param arr: unsort array
    :param low: the start position of arr
    :param high: the end position of arr
    :return: the pivot position
    """
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quick_sort(arr, low, high):
    """
    implement of quick sort
    time complexity O(nLogn)
    best case: partition() return the middle element of arr as pivot, O(Logn)
    worst case: the arr is already sorted, O(n2)
    :param arr: unsort array
    :param low: array start point
    :param high: array end point
    :return: sorted array
    """
    if low < high:
        index = partition(arr, low, high)
        # index = partition2(arr, low, high)
        quick_sort(arr, low, index - 1)
        quick_sort(arr, index + 1, high)


def test():
    A = [64, 25, 12, 22, 11]
    quick_sort(A, 0, len(A) - 1)
    print("Sorted array")
    for i in range(len(A)):
        print("%d" % A[i])
