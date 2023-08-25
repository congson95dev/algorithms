"""
Bài toán:
Cho 1 array activity = [[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9]] với các element gồm start và finish
Cần tìm tối đa các element mà start của element sau phải > start của element trước
Ý tưởng:
Sort array đã cho theo finish
Lấy phần tử đầu tiên và lặp lần lượt để tìm phần tử tiếp theo có start >= finish của phần tử trước đó
"""


def max_activities(arr):
    result = []

    arr.sort(key=lambda x: x[1])  # sort by element with index 1 of the each element inside array, which is "finish"
    print("Activity after sort: ")
    print(arr)

    i = 0
    result.append(arr[i])

    for j in range(1, len(arr)):
        if arr[j][0] >= arr[i][1]:
            result.append(arr[j])
            i = j
    return result


if __name__ == '__main__':
    # generate an array with "start" and "finish"
    activity = [[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9]]

    result = max_activities(activity)
    print("Result: ")
    print(result)