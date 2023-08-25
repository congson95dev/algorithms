"""
Ý tưởng: 
lấy phần tử đầu tiên làm pivot, 
sau đó lấy ra các phần tử nhỏ hơn pivot thành 1 array khác gọi là arr1, 
lấy các phần tử lớn hơn pivot cho vào arr2. 
Sau đó, chạy đệ quy quicksort để làm tương tự với arr1 và arr2
"""


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        # Lấy phần tử ở giữa làm pivot
        pivot_index = len(array) // 2  
        pivot = array[pivot_index]
        less = [i for i in array if i < pivot]
        greater = [i for i in array if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([1, 2, 3, 5, 10, 15, 19, 25]))
