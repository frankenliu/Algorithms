def merge(arr, l, m, r):
    """
    merge the part sort array
    :param arr: source array
    :param l: the start position
    :param m:  the middle position, divide the arr to two part sort array
    :param r: the end position
    :return: None
    """
    n1 = (m - l + 1)
    n2 = (r - m)
    arr_l = [0] * n1
    arr_r = [0] * n2

    for i in range(0, n1):
        arr_l[i] = arr[l + i]
    for j in range(0, n2):
        arr_r[j] = arr[m + 1 + j]

    k = 0
    t = 0
    p = l
    while k < n1 and t < n2:
        if arr_l[k] < arr_r[t]:
            arr[p] = arr_l[k]
            k += 1
        else:
            arr[p] = arr_r[t]
            t += 1
        p += 1
    while k < n1:
        arr[p] = arr_l[k]
        p += 1
        k += 1
    while t < n2:
        arr[p] = arr_r[t]
        p += 1
        t += 1


def merge_sort(arr, l, r):
    """
    implement the merge sort
    :param arr: unsort array
    :param l: the start position
    :param r: the end position
    :return: None
    """
    if l < r:
        mid = l + int((r - l) / 2)
        merge_sort(arr, l, mid)
        merge_sort(arr, mid+1, r)
        merge(arr, l, mid, r)


def test():
    A = [64, 25, 12, 22, 11]
    merge_sort(A, 0, len(A) - 1)
    print("Merge sort:Sorted array")
    for i in range(len(A)):
        print("%d" % A[i])