"""
Bài toán:
Cho 1 list items gồm "size" và "value": items = ((22, 19), (10, 9), (9, 9), (7, 6))
Cần tìm tối đa element với tổng value lớn nhất sao cho tổng size n, ví dụ là < 25

Ý tưởng:
Tính ratio theo value / size của từng element, sau đó sort theo ratio
Loop list items đã sort ở trên, và lần lượt cộng size và value từng element vào tổng size và tổng value
sao cho k vượt quá 25,
sau đó khi không thể cộng thêm thì ta sẽ tính % của phần tử cuối đó sao cho khi cộng với tổng size thì vừa đủ 25,
và thêm % đó vào tổng value.

VD: phần tử cuối đó là (22, 19), và tổng size đang đếm hiện đang là 19,
vậy thì cần lấy (25 - 19) / 22 để lấy được % size còn có thể nhét vào,
sau đó nhân với value => * 19 => 5.18 => đây là value có thể nhét nốt vào để đủ size = 25.

Lưu ý: với trường hợp của Fractional Knapsach Problem thì ta có thể áp dụng được Greedy Algorithms,
bởi vì bài toán này cho phép lấy dư, còn nếu nó k cho phép lấy dư, thì sẽ k thể áp dụng Greedy Algorithms
"""


def algorithm(items, capacity):
    # calculate ratio by value / size
    ratio_list = [(size, value, value / size) for size, value in items]
    # sorted by ratio, from highest to lowest
    ratio_list = sorted(ratio_list, key=lambda tup: tup[2], reverse=True)
    print(ratio_list)

    total_size = total_value = 0
    for size, value, ratio in ratio_list:
        new_size = total_size + size
        if new_size > capacity:
            break
        total_size = new_size
        total_value += value
    else:
        return total_value  # if run to the end of the for loop without break, we will return total_value
    return total_value + (capacity - total_size) / size * value  # return total value + percent valid of last item


# generate items with "size" and "value"
items = ((22, 19), (10, 9), (9, 9), (7, 6))
capacity = 25

print(algorithm(items, capacity))  # result: 23.18181818181818
