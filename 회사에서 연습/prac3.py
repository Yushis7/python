data = [1,2,3,4,5,"a"]
print(len(data))

numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)  # 출력: [2, 4, 6, 8]


a = [1,2,3,4,"a"]
b = list(map(lambda x:x*2 , a))
print(b)

a = [1,2,3,4]
b = list(map(lambda x: x+2 , a))
print(b)


a = [1,2,3,4,5]
b = list(filter(lambda x: x -2 == 0, a))
print(b)

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 출력: [2, 4]

a = [1,4,2,5,6]
print(sorted(a))

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)
# 출력: 
# 0 apple
# 1 banana
# 2 cherry

names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 95]
for name, score in zip(names, scores):
    print(name, score)
# 출력:
# Alice 85
# Bob 90
# Charlie 95


numbers = [1, 2, 2, 3, 4, 4,"a","a"]
unique_numbers = set(numbers)
print(unique_numbers)  # 출력: {1, 2, 3, 4}


arr = [38, 27, 43, 3, 9, 82, 10]
def merge_sort(arr):
    print(merge_sort(arr))


# 데이터베이스 설정값
db_config = ("localhost", 3306, "root", "password")

# db_config[1] = 5432  # 오류 발생: 'tuple' object does not support item assignment

print(db_config)
# ('localhost', 3306, 'root', 'password')

db_config = ("localhost", 3306, "root", "password")
db_config = (db_config[0], 5432, db_config[2], db_config[3])  # 새 튜플 생성
print(db_config)
# ('localhost', 5432, 'root', 'password')

db_config = ("localhost", 3306, "root", "password")
db_config[1] = 1234
print(db_config)


i = 1
while i <= 5:
    print(i)
    i += 1
    
    
# 순차 검색 구현 예시
# 배열에서 특정 값을 찾는 순차 검색 알고리즘입니다.

def linear_search(arr, target):
    # 배열의 각 요소를 하나씩 검사합니다.
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # 요소를 찾으면 인덱스를 반환합니다.
    return -1  # 요소를 찾지 못한 경우 -1을 반환합니다.

# 배열과 찾고자 하는 값
arr = [64, 34, 25, 12, 22, 11, 90]
target = 25

# 순차 검색 수행
result = linear_search(arr, target)
if result != -1:
    print(f"값 {target}은(는) 인덱스 {result}에 있습니다.")
else:
    print(f"값 {target}을(를) 찾을 수 없습니다.")
    




def validate_username(username):
    if len(username) < 3:
        return "사용자 이름은 최소 3자 이상이어야 합니다."
    else:
        return "사용자 이름이 유효합니다."

# 사용자 입력 예시
username1 = "레옹"
username2 = "마틸다"

print(validate_username(username1))
# 출력: 사용자 이름은 최소 3자 이상이어야 합니다.

print(validate_username(username2))
# 출력: 사용자 이름이 유효합니다.



# break 예시
for i in range(1, 10):
    if i == 5:
        break
    print(i)
#5가 되면 스탑

# continue 예시
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)
#짝수는 건너뛰기

#구구단 만들기
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")
    print()  # 단 사이에 빈 줄 출력
    
    
for i in range(2 ,10):
    for j in range(1 in 10):
        print(f"{i} x {j} = {i*j}")
    print()
    
    
# # 일반적인 for 루프
# squares = []
# for i in range(10):
#     squares.append(i**2)

# # 리스트 컴프리헨션
# squares = [i**2 for i in range(10)]

# print(squares)


# 비효율적인 방법
for i in range(1000000):
    result = i * len([1, 2, 3, 4, 5])

# 효율적인 방법
list_length = len([1, 2, 3, 4, 5])
for i in range(1000000):
    result = i * list_length
print(result)


data = [23, 45, 67, 89, 12]
for i in range(len(data)):
    print(f"데이터 {i}번: {data[i]}")
    
    
# 선택 정렬 예시 코드 
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 버블 정렬 예시 코드
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 퀵 정렬 예시 코드
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)



# 병합 정렬 예시 코드
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

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


# 인접 행렬 예제
# 노드 0~4가 있다고 가정        
n = 5  # 노드 개수
graph = [[0] * n for _ in range(n)]

# 간선 추가 (무방향 그래프)
edges = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 4)]
for u, v in edges:
    graph[u][v] = 1
    graph[v][u] = 1  # 무방향 그래프이므로 대칭

# 그래프 출력
for row in graph:
    print(row)


# Python을 사용한 N-Queens 문제 해결 예시

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens(board, col, n):
    if col >= n:
        return True
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_nqueens(board, col + 1, n):
                return True
            board[i][col] = 0
    return False

def nqueens(n):
    board = [[0] * n for _ in range(n)]
    if solve_nqueens(board, 0, n):
        for row in board:
            print(row)
    else:
        print("Solution does not exist")

nqueens(4)



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



#다음(Daum)의 주가가 89,000원이고 네이버(Naver)의 주가가 751,000원이라고 가정하고, 어떤 사람이 다음 주식 100주와 네이버 주식 20주를 가지고 있을 때 그 사람이 가지고 있는 주식의 총액을 계산하는 프로그램을 작성하세요.

naver= 751000
daum = 89000
total = naver*20+daum*100
print(total)

# 위에서 구한 주식 총액에서 다음과 네이버의 주가가 각각 5%, 10% 하락한 경우에 손실액을 구하는 프로그램을 작성하세요.
loss = naver*0.1*20+daum*0.05*100
print(loss)

#우리나라는 섭씨 온도를 사용하는 반면 미국과 유럽은 화씨 온도를 주로 사용합니다. 화씨 온도(F)를 섭씨 온도(C)로 변환할 때는 다음과 같은 공식을 사용합니다. 이 공식을 사용해 화씨 온도가 50일 때의 섭씨 온도를 계산해 보세요.
#C = (F-32)/1.8

F = 50
C = (F-32)/1.8
print(C)

#화면에 "pizza"를 10번 출력하는 프로그램을 작성하세요.
print("pizza\n" *10)

#월요일에 네이버의 주가가 100만 원으로 시작해 3일 연속으로 하한가(-30%)를 기록했을 때 수요일의 종가를 계산해 보세요.
naver = 1000000
월요일 = naver*0.7
화요일 = 월요일*0.7
수요일 = 화요일*0.7
print(수요일)

#s라는 변수에 'Daum KaKao'라는 문자열이 바인딩돼 있다고 했을 때 문자열의 슬라이싱 기능과 연결하기를 이용해 s의 값을 'KaKao Daum'으로 변경해 보세요.
s = 'Daum kakao'
s = s[5:]+""+s[:4]
print(s)

# a라는 변수에 'hello world'라는 문자열이 바인딩돼 있다고 했을 때 a의 값을 'hi world'로 변경해 보세요.
a = "hello world"
print(a.replace("hello","hi"))


#x라는 변수에 'abcdef'라는 문자열이 바인딩돼 있다고 했을 때 x의 값을 'bcdefa'로 변경해 보세요.
x = 'abcdef'
x = x[1:]+x[0]
print(x)


def cal_upper(price):
    increment = price * 0.3
    upper_price = price + increment
    return upper_price

cal_upper(100)

print(cal_upper)



upper_price = cal_upper(1000)
print(upper_price)

upper_price = cal_upper(5000)
print(upper_price)



def myaverage(a,b):
        return (a+b)/2
    
print(myaverage(3,4))



url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])

string = 'abcdfe2a354a32a'
print(string.replace('a','A'))





name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")


name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))


name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))


#삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
#상장주식수 = "5,969,782,550"

상장주식수 = "5,969,782,550"
컴마제거 = 상장주식수.replace(",","")
print(컴마제거)
형태변환 = int(컴마제거)
print(형태변환,type( 형태변환))


#문자열의 좌우의 공백이 있을 때 이를 제거해보세요.
data = "   삼성전자    "
data1 = data.strip
print(data1)




