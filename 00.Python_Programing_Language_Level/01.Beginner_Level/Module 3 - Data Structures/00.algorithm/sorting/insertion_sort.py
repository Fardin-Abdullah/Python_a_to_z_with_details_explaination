def insertion_sort(A):
    n = len(A)

    for i in range(1,n):
        item = A[i]
        j = i - 1

        while j >= 0 and A[j] > item :
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = item

if __name__ == "__main__":
    A = [5,2,4,6,1,3]
    print("Before Sort:",A)
    insertion_sort(A)
    print("After Sort:",A)