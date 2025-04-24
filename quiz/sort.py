def bubble_sort(arr):
    print("\nProses Bubble Sort:")
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
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
            print(f"Langkah {i}.{j + 1}: {a}")
        a[j + 1] = key
        print(f"Setelah penyisipan {i}: {a}")
    print(f"Hasil akhir Insertion Sort: {a}")

def selection_sort(arr):
    print("\nProses Selection Sort:")
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[min_idx] < a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        print(f"Langkah {i}: {a}")
    print(f"Hasil akhir Selection Sort: {a}")
    
def quick_sort_with_steps(arr):
    a = arr.copy()
    low = 0
    high = len(a) - 1

    def quick_sort(a, low, high):
        if low < high:
            pivot_index = partition(a, low, high)
            quick_sort(a, low, pivot_index)
            quick_sort(a, pivot_index + 1, high)

    def partition(arr, low, high):
        print(f"\nMulai partition: {arr[low:high+1]}")
        i = low - 1
        j = high + 1

        while True:
            # i ke kanan
            i += 1
            while arr[i] < arr[low]:
                i += 1

            # j ke kiri
            j -= 1
            while arr[j] > arr[low]:
                j -= 1

            print(f"  i = {i} ({arr[i]}), j = {j} ({arr[j]})")

            if i >= j:
                print(f"  → i >= j, return {j}")
                return j

            print(f"  Tukar arr[{i}] = {arr[i]} dan arr[{j}] = {arr[j]}")
            arr[i], arr[j] = arr[j], arr[i]
            print(f"  Setelah tukar: {arr}")

    print("Proses Quick Sort:")
    quick_sort(a, low, high)
    print("\nHasil akhir Quick Sort:", a)


if __name__ == "__main__":
    choice_input = input("Gunakan data default atau input manual? (d/m): ")
    if choice_input == "d":
        data = [5,5,7,6,8,7,4,7]
    elif choice_input == "m":
        raw_input = input("Masukkan angka-angka (pisahkan dengan koma): ")
        try:
            data = [int(x.strip()) for x in raw_input.split(',') if x.strip()]
        except ValueError:
            print("⚠️ Input harus berupa angka yang dipisahkan koma.")
            exit()
    else:
        print("⚠️ Input tidak valid.")
        exit()
    

    bubble_sort(data)
    insertion_sort(data)
    selection_sort(data)
    quick_sort_with_steps(data)
