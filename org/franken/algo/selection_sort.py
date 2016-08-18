def selection_sort(arr):
    if len(arr) <= 1:
        return

    for i in range(len(arr)):
        pos = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[pos]:
                pos = j
        arr[i], arr[pos] = arr[pos], arr[i]


def test():
    A = [64, 25, 12, 22, 11]
    selection_sort(A)
    print("Sorted array")
    for i in range(len(A)):
        print("%d" % A[i])