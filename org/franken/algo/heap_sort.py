def heapify(arr, n):
    """
    find the largest element of the array and
    move it to the last place
    :param arr: unsort array
    :param n: the unsort number of the arr
    :return: none
    """
    mid = (int)(n / 2 - 1)
    for i in range(mid, - 1, -1):
        large = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[l] > arr[large]:
            large = l
        if r < n and arr[r] > arr[large]:
            large = r
        if large != i:
            arr[i], arr[large] = arr[large], arr[i]
    arr[0], arr[n-1] = arr[n-1], arr[0]


def heap_sort(arr):
    """
    implement of the heap sort
    time complexity O(nLogn) both worst and best case
    space complexity O(1)
    :param arr: unsort array
    :return: none
    """
    n = len(arr)
    for i in range(n):
        heapify(arr, n - i)


def test():
    A = [64, 25, 12, 22, 11]
    heap_sort(A)
    print("Sorted array")
    for i in range(len(A)):
        print("%d" % A[i])