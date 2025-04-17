def bubble_sort(arr):
    print("\nProses Bubble Sort:")
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] < a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
            print(f"Langkah {i}.{j}: {a}")
    print(f"Hasil akhir Bubble Sort: {a}")

def insertion_sort(arr):
    print("\nProses Insertion Sort:")
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key > a[j]:
            a[j + 1] = a[j]
            j -= 1
            print(f"Langkah {i}.{j+1}: {a}")
        a[j + 1] = key
        print(f"Setelah penyisipan {i}: {a}")
    print(f"Hasil akhir Insertion Sort: {a}")

def selection_sort(arr):
    print("\nProses Selection Sort:")
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if a[min_idx] < a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        print(f"Langkah {i}: {a}")
    print(f"Hasil akhir Selection Sort: {a}")

data = [155, 142, 85, 176, 78, 36, 32, 59, 37, 169, 38, 55, 62, 68, 49, 69, 91]

bubble_sort(data)
insertion_sort(data)
selection_sort(data)
