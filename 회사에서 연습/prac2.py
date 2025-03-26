numbers = [10, 20, 30]
print(sum(numbers))  # 출력: 60


# with open('sample.txt', 'r') as file:
#     content = file.read()
#     print(content)

for i in range(5):
    print(i)
# 출력: 0, 1, 2, 3, 4

numbers = [1, 2, 2, 3, 4, 4]
unique_numbers = set(numbers)
print(unique_numbers)  # 출력: {1, 2, 3, 4}


numbers = [0, 1, 2, 3]
print(any(numbers))  # 출력: True
print(all(numbers))  # 출력: False


name = "Alice"
age = 25
print("Name: {}, Age: {}".format(name, age))
# 출력: Name: Alice, Age: 25

add = lambda x, y: x + y
print(add(5, 3))  # 출력: 8


from functools import reduce
numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x * y, numbers)
print(result)  # 출력: 24


# Python을 사용한 간단한 분할 정복 예시: 병합 정렬 구현

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))

inventory = {
    "apple": 50,
    "banana": 30,
    "orange": 20
}

# 새로운 상품이 입고되었을 때
inventory["apple"] += 10  # 사과 재고 추가
inventory["banana"] -= 5  # 바나나 재고 감소

print(inventory)
# 출력: {'apple': 60, 'banana': 25, 'orange': 20}

10

