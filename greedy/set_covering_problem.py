"""
Bài toán:
Cho 1 list các đỉnh và 1 list các set gồm các đỉnh mà nó bao phủ
universe = set(range(1, 11))
subsets = [
    set([1, 2, 3, 4, 5]),
    set([4, 5, 6, 7]),
    set([2, 6, 8, 9, 10]),
    set([1, 3, 8, 10]),
    set([5, 7, 9])
]
Tìm các cặp sao cho tập hợp các cặp này có thể bao phủ toàn bộ các đỉnh đã cho và với số lượng các cặp là nhỏ nhất.
Kết quả: set([1, 2, 3, 4, 5]), set([2, 6, 8, 9, 10]), set([4, 5, 6, 7]),
bởi đây là tập hợp các cặp chứa số từ 1->10, chỉ với 3 cặp.

Ý tưởng:
Tạo 1 biến tạm remaining_elements nhớ các đỉnh còn lại chưa được bao phủ.
Tìm các cặp với độ bao phủ là rộng nhất và k nằm trong remaining_elements
Thêm cặp tìm được vào kết quả
xóa các đỉnh đã được bao phủ khỏi remaining_elements
"""


def set_cover(universe, subsets):
    if not subsets:
        return None

    cover = set()
    remaining_elements = set(universe)

    while remaining_elements:
        # tìm subset trong list subsets mà có nhiều phần tử không nằm trong remaining_elements nhất
        subset = max(subsets, key=lambda s: len(s.intersection(remaining_elements)))
        cover.add(frozenset(subset))
        remaining_elements -= subset

    return cover


# Test Case 1
universe = set(range(1, 11))
subsets = [
    set([1, 2, 3, 4, 5]),
    set([4, 5, 6, 7]),
    set([2, 6, 8, 9, 10]),
    set([1, 3, 8, 10]),
    set([5, 7, 9])
]

result = set_cover(universe, subsets)
print("Set Cover:", result)  # result: frozenset({1, 2, 3, 4, 5}), frozenset({2, 6, 8, 9, 10}), frozenset({4, 5, 6, 7})

# Test Case 2
universe = set(range(1, 6))
subsets = [
    set([1, 2]),
    set([2, 3]),
    set([3, 4]),
    set([4, 5])
]

result = set_cover(universe, subsets)
print("Set Cover:", result)  # result: {frozenset({3, 4}), frozenset({4, 5}), frozenset({1, 2})}

# Test Case 3
universe = set(range(1, 6))
subsets = [
    set([1, 2]),
    set([2, 3]),
    set([3, 4]),
    set([4, 5]),
    set([1, 2, 3, 4, 5])
]

result = set_cover(universe, subsets)
print("Set Cover:", result)  # result: {frozenset({1, 2, 3, 4, 5})}
